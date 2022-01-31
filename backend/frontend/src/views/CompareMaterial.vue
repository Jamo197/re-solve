<template>
  <div>
    <div v-if="!filteredMaterials.results">
      <!-- Masthead-->
      <header class="masthead-compare">
        <div class="container">
          <div class="masthead-compare-subheading">
            Materialien vergleichen!
          </div>
          <div class="masthead-compare-heading text-uppercase">
            Finden Sie ihr perfektes Material
          </div>
          <a class="btn btn-primary btn-xl text-uppercase" href="#searchForm"
            >Starten</a
          >
        </div>
      </header>
      <!-- Services-->
      <section class="page-section material-page" id="searchForm">
        <div class="container material-page">
          <div class="text-center">
            <h2 class="section-heading text-uppercase">
              Nachhaltige Lösungen für Ihr Unternehmen
            </h2>
            <h3 class="section-subheading text-muted">
              Finden Sie mit re:solve umweltfreundliche Materialalternativen.
            </h3>
          </div>
          <form @submit.prevent="onSubmit">
            <div class="row align-items-stretch mb-3">
              <div class="col-md-6">
                <div class="form-group">
                  <input
                    v-model="searchParams.articleName"
                    class="form-control"
                    id="articleName"
                    type="text"
                    placeholder="Artikelname"
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <select
                    class="form-select"
                    v-model="searchParams.materialClass"
                    aria-label="Default select example"
                  >
                    <option selected disabled value="">Materialklasse</option>
                    <option
                      v-for="material_class in materialClassData"
                      :key="material_class.type"
                      :value="material_class.type"
                    >
                      {{ material_class.type }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
            <div class="row align-items-stretch mb-3">
              <div class="col-md-4">
                <input
                  v-model="searchParams.articleDepth"
                  class="form-control"
                  id="depth"
                  type="text"
                  placeholder="Materialstärke in mm"
                />
              </div>
              <div class="col-md-4">
                <input
                  v-model="searchParams.articleLength"
                  class="form-control"
                  id="length"
                  type="text"
                  placeholder="Länge in mm"
                />
              </div>
              <div class="col-md-4">
                <input
                  v-model="searchParams.articleWidth"
                  class="form-control"
                  id="width"
                  type="text"
                  placeholder="Breite in mm"
                />
              </div>
            </div>
            <div class="row align-items-stretch mb-3">
              <div class="col-md-6">
                <div class="form-group">
                  <select
                    class="form-select"
                    v-model="selectedMaterialName"
                    aria-label="Default select example"
                    v-on:change="setSelectedMaterial"
                  >
                    <option selected value="">
                      Materialeigenschaften wie ...
                    </option>
                    <option
                      v-for="material in materials"
                      :key="material.name"
                      :value="material.name"
                    >
                      {{ material.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-md-6" v-if="selectedMaterialName">
                <h5 class="selected-material">
                  Löschen Sie unwichtige Eigenschaften, um bessere Ergebnisse zu
                  bekommen!
                </h5>
              </div>
            </div>
            <div class="row align-items-stretch mb-3">
              <div class="col-md-5">
                <div class="form-group">
                  <select
                    class="form-select"
                    v-model="materialProperty.property_name"
                    aria-label="Default select example"
                    v-on:change="setMaterialPropValues"
                  >
                    <option selected disabled value="">
                      Materialeigenschaft
                    </option>
                    <option
                      v-for="prop in propertyData"
                      :key="prop.type"
                      :value="prop.type"
                    >
                      {{ prop.type }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-md-1">
                <button
                  class="btn btn-primary btn-x1"
                  :disabled="isDisabled"
                  v-on:click="addNewProperty"
                >
                  <i class="fa fa-plus"></i>
                </button>
              </div>
              <div class="col-md-6" v-if="materialProperty.property_name">
                <input
                  v-model="materialProperty.value"
                  class="form-control"
                  id="articleName"
                  type="text"
                  :placeholder="'Wert in ' + materialProperty.unit"
                />
              </div>
            </div>
            <div v-if="searchParams.materialProperties.length">
              <div
                class="row align-items-stretch mb-3"
                v-for="matProb in searchParams.materialProperties"
                :key="matProb.property_name"
              >
                <div class="col-md-5">
                  <div class="form-group">
                    <select
                      class="form-select"
                      v-model="matProb.property_name"
                      aria-label="Default select example"
                    >
                      <option selected disabled value="">
                        Materialeigenschaft
                      </option>
                      <!-- TODO: @change="changeProperty(matProb)" kann disabled rausnehmen, wenn in select ein :change reinkommt, um die Value zu wechseln -->
                      <option
                        disabled
                        v-for="prop in propertyData"
                        :key="prop.type"
                        :value="prop.type"
                      >
                        {{ prop.type }}
                      </option>
                    </select>
                  </div>
                </div>
                <div class="col-md-1">
                  <button
                    class="btn btn-danger btn-x1"
                    v-on:click="deleteProperty(matProb)"
                  >
                    <i class="fas fa-trash-alt"></i>
                  </button>
                </div>
                <div class="col-md-6" v-if="matProb.property_name">
                  <input
                    v-model="matProb.value"
                    class="form-control"
                    id="articleName"
                    type="text"
                    :placeholder="'Wert in ' + matProb.unit"
                  />
                </div>
              </div>
            </div>
            <div class="row align-items-stretch mb-3">
              <div class="offset-6 col-md-6">
                <div class="form-group">
                  <div class="form-check">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      v-model="searchParams.sustainableMaterials"
                      id="sustainableMaterialsChecked"
                      checked
                    />
                    <label
                      class="form-check-label"
                      for="sustainableMaterialsChecked"
                    >
                      Nachhaltigere Materialien anzeigen?
                    </label>
                  </div>
                </div>
              </div>
            </div>

            <div class="row align-items-stretch mb-3">
              <div class="offset-10 col-md-2">
                <div class="form-group">
                  <button type="submit" class="btn btn-success my-3">
                    Material suchen!
                  </button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </section>
    </div>

    <div v-if="filteredMaterials.results">
      <MaterialResultComponent
        :articles="filteredMaterials.articles"
        :sustainableArticle="searchParams.sustainableMaterials"
        @change="resetParams"
      />
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";
import MaterialResultComponent from "@/components/MaterialResultComponent.vue";
import PropertyData from "@/assets/data/propertyData.json";
import MaterialClassData from "@/assets/data/materialClassData.json";
export default {
  name: "CompareMaterial",
  components: {
    MaterialResultComponent,
  },
  data() {
    return {
      propertyData: PropertyData,
      materialClassData: MaterialClassData,
      materials: {},
      searchParams: {
        articleName: "",
        articleDepth: "",
        articleLength: "",
        articleWidth: "",
        materialClass: "",
        materialProperties: [],
        sustainableMaterials: true,
      },
      selectedMaterialName: "",
      materialProperty: {
        property_name: "",
        value: "",
        nameForFilter: "",
        unit: "",
      },
      filteredMaterials: {
        results: false,
        articles: [],
      },
    };
  },
  methods: {
    addNewProperty() {
      this.searchParams.materialProperties.push(
        JSON.parse(JSON.stringify(this.materialProperty))
      );
      this.materialProperty.property_name = "";
      this.materialProperty.nameForFilter = "";
      this.materialProperty.value = "";
      this.materialProperty.unit = "";
    },
    deleteProperty(element) {
      var propIndex = this.searchParams.materialProperties.indexOf(element);
      this.searchParams.materialProperties.splice(propIndex, 1);
      if (!this.searchParams.materialProperties.length) {
        this.selectedMaterialName = "";
      }
    },
    // TODO: Noch nicht in Gebrauch
    changeProperty(element) {
      var propIndex = this.searchParams.materialProperties.indexOf(element);
      this.searchParams.materialProperties[propIndex].property_name =
        element.type;
    },
    setPropertyValue(property) {
      var selectedProperty = PropertyData.find(
        (element) => element.type == property.property_name
      );
      this.materialProperty.unit = selectedProperty.unit;
      this.materialProperty.nameForFilter = selectedProperty.nameForFilter;
    },
    setMaterialPropValues() {
      this.setPropertyValue(this.materialProperty);
    },
    setSelectedMaterial() {
      this.searchParams.materialProperties = [];
      if (this.selectedMaterialName != "") {
        var selectedMaterial = this.materials.find(
          (element) => element.name == this.selectedMaterialName
        );
        for (const property of selectedMaterial.properties) {
          if (property.value != 0) {
            this.materialProperty.property_name = property.property_name;
            this.materialProperty.value = property.value;
            this.setPropertyValue(property);
            this.addNewProperty();
          }
        }
      }
    },
    setFilterEndpoint() {
      var filterParams = "?";
      if (this.searchParams.articleName) {
        filterParams += "article_name=" + this.searchParams.articleName + "&";
      }
      if (this.searchParams.articleDepth) {
        filterParams += "article_depth=" + this.searchParams.articleDepth + "&";
      }
      if (this.searchParams.articleLength) {
        filterParams += "article_length=" + this.searchParams.articleLength + "&";
      }
      if (this.searchParams.articleWidth) {
        filterParams += "article_width=" + this.searchParams.articleWidth + "&";
      }
      if (this.searchParams.materialClass) {
        filterParams +=
          "material_class=" + this.searchParams.materialClass + "&";
      }
      if (this.searchParams.materialProperties) {
        for (const property of this.searchParams.materialProperties) {
          filterParams += property.nameForFilter + "=" + property.value + "&";
        }
      }
      return filterParams;
    },
    async onSubmit() {
      if (!this.isDisabled) {
        this.addNewProperty();
      }
      let endpoint = "/api/filter/articles/";
      try {
        endpoint += this.setFilterEndpoint();
        console.log(endpoint);
        const response = await axios.get(endpoint);
        this.filterParams = this.searchParams;
        this.filteredMaterials.articles = response.data;
        this.filteredMaterials.results = true;
      } catch (error) {
        console.log(error.response);
        alert("Ein Fehler ist aufgetreten!\n", error.response.statustext);
      }
    },
    async loadMaterials() {
      let endpoint = "/api/materials/";
      try {
        const response = await axios.get(endpoint);
        this.materials = response.data;
      } catch (error) {
        console.log(error.response);
        alert("Ein Fehler ist aufgetreten!\n", error.response.statustext);
      }
    },
    resetParams(reset) {
      if (reset) {
        this.filteredMaterials.results = false;
        this.filteredMaterials.articles = [];
        this.searchParams.articleName = "";
        this.searchParams.articleDepth = "";
        this.searchParams.articleWidth = "";
        this.searchParams.articleLength = "";
        this.searchParams.materialClass = "";
        this.searchParams.materialProperties = [];
        this.searchParams.sustainableMaterials = true;
        this.materialProperty.property_name = "";
        this.materialProperty.value = "";
        this.selectedMaterialName = "";
      } else if (!reset) {
        this.filteredMaterials.results = false;
      }
    },
  },
  computed: {
    isDisabled() {
      return !(
        this.materialProperty.property_name && this.materialProperty.value
      );
    },
  },
  created() {
    this.loadMaterials();
    this.resetParams();
  },
};
</script>