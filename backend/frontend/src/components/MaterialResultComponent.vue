<template>
  <div>
    <!-- Masthead-->
    <header class="masthead-compare">
      <div class="container">
        <!-- <div class="masthead-compare-subheading">Wir haben die beste Lösung für Sie gefunden!</div> -->
        <div class="masthead-compare-heading text-uppercase">
          Wir haben die beste Lösung für Sie gefunden!
        </div>
        <button
          class="btn btn-primary btn-xl text-uppercase"
          v-on:click="backToSearch(true)"
        >
          Neue Suche
        </button>
      </div>
    </header>
    <section class="page-section material-page" id="results">
      <div
        class="container shadow p-3 mb-5 bg-white rounded"
        v-if="articles.length > 0"
      >
        <div class="row align-items-stretch mb-3">
          <!-- TODO: Vertical align image -->
          <div class="col-md-4">
            <img
              src="@/assets/img/logos/resolve_no_background.png"
              style="width: auto; height: auto"
              alt="re:solve Logo"
            />
          </div>
          <div class="col-md-8 material-page">
            <div class="row align-items-stretch mb-3">
              <div class="col-md-9">
                <div class="text-subheading section-heading">
                  <h2>{{ bestArticle.name }}</h2>
                </div>
              </div>
              <div class="col-md-3">
                <div class="text-subheading section-heading eco-score">
                  <h3>
                    <a
                      class="eco-score-pointer"
                      v-on:click="showModal(bestArticle)"
                    >
                      <i
                        :class="{
                          'fas fa-leaf': true,
                          'eco-score-1': bestArticle.ecological_index <= 1,
                          'eco-score-2':
                            bestArticle.ecological_index > 1 &&
                            bestArticle.ecological_index <= 2,
                          'eco-score-3':
                            bestArticle.ecological_index > 2 &&
                            bestArticle.ecological_index <= 3,
                          'eco-score-4':
                            bestArticle.ecological_index > 3 &&
                            bestArticle.ecological_index <= 4,
                          'eco-score-5':
                            bestArticle.ecological_index > 4 &&
                            bestArticle.ecological_index < 5,
                          'eco-score-6': bestArticle.ecological_index == 5,
                        }"
                      ></i>
                      {{ bestArticle.ecological_index.toFixed(1) }}/5
                    </a>
                  </h3>
                </div>
              </div>
            </div>
            <div class="row align-items-stretch mb-3">
              <div class="col-md-12">
                <p>{{ bestArticle.description }}</p>
                <p>
                  <span class="fw-bold">Materialstärke: </span
                  >{{ bestArticle.depth }}mm <span class="fw-bold">Maße: </span
                  >{{ bestArticle.length }}mm x {{ bestArticle.width }}mm
                </p>
              </div>
            </div>
            <div class="row align-items-stretch mb-3">
              <div class="col-md-6">
                <div class="text-center">
                  <p class="fw-bold">Materialeigenschaften</p>
                </div>
                <div
                  class="row align-items-stretch"
                  v-for="property in bestArticle.material.properties"
                  :key="property.id"
                >
                  <div class="col-md-6">
                    <span>{{ property.property_name }}:</span>
                  </div>
                  <div class="col-md-6">
                    <span>{{ property.value }} {{ property.unit }}</span>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="text-center">
                  <p class="fw-bold">Nachhaltigkeitseigenschaften</p>
                </div>
                <div
                  class="row align-items-stretch"
                  v-for="sustain_property in bestArticle.material
                    .sustainability_properties"
                  :key="sustain_property.id"
                >
                  <div class="col-md-6">
                    <span>{{ sustain_property.property_name }}:</span>
                  </div>
                  <div class="col-md-6">
                    <span
                      >{{ sustain_property.value }}
                      {{ sustain_property.unit }}</span
                    >
                  </div>
                </div>
              </div>
            </div>
            <!-- TODO: Hier Button -->
            <div class="col-md-12 material-page mb-3">
              <div class="d-grid gap-2">
                <button
                  class="btn btn-success"
                  v-on:click="addToCart(bestArticle)"
                >
                  Zum Warenkorb hinzufügen
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="text-center mb-3">
          <h2 v-if="articles.length > 0">
            Materialien mit ähnlichen Eigenschaften
          </h2>
          <h2 v-if="articles.length == 0">
            Keine Artikel mit Ihren Spezifikationen gefunden! Passen Sie
            gegebenfalls Ihre Suche an.
          </h2>
        </div>
        <div class="row align-items-stretch mb-3">
          <div
            class="col-md-4"
            v-for="article in articles.slice(1)"
            :key="article.id"
          >
            <div class="card mb-3">
              <!-- <div class="card-header">Featured</div> -->
              <div class="card-body">
                <h5 class="card-title">
                  <div class="row align-items-stretch mb-3">
                    <div class="col text-start">
                      {{ article.name }}
                    </div>
                    <div class="col text-end">
                      <a
                        class="eco-score-pointer"
                        v-on:click="showModal(article)"
                      >
                        <i
                          :class="{
                            'fas fa-leaf': true,
                            'eco-score-1': article.ecological_index <= 1,
                            'eco-score-2':
                              article.ecological_index > 1 &&
                              article.ecological_index <= 2,
                            'eco-score-3':
                              article.ecological_index > 2 &&
                              article.ecological_index <= 3,
                            'eco-score-4':
                              article.ecological_index > 3 &&
                              article.ecological_index <= 4,
                            'eco-score-5':
                              article.ecological_index > 4 &&
                              article.ecological_index < 5,
                            'eco-score-6': article.ecological_index == 5,
                          }"
                        ></i>
                        {{ article.ecological_index.toFixed(1) }}/5
                      </a>
                    </div>
                  </div>
                </h5>
                <hr />
                <!-- <p class="card-text">
                  {{ article.description }}
                </p> -->
                <p class="my-0">
                  <span class="fw-bold">Materialstärke: </span
                  >{{ article.depth }}mm
                </p>
                <p class="my-0">
                  <span class="fw-bold">Maße: </span>{{ article.length }}mm x
                  {{ article.width }}mm
                </p>
                <div
                  class="row align-items-stretch"
                  v-for="prop in article.material.properties"
                  :key="prop.id"
                >
                  <div class="col-md-6">
                    <p class="card-text">{{ prop.property_name }}</p>
                  </div>
                  <div class="col-md-6">
                    <p class="card-text">{{ prop.value }} {{ prop.unit }}</p>
                  </div>
                </div>
                <hr />
                <div
                  class="row align-items-stretch"
                  v-for="sustain_prop in article.material
                    .sustainability_properties"
                  :key="sustain_prop.id"
                >
                  <div class="col-md-6">
                    <p class="card-text">{{ sustain_prop.property_name }}</p>
                  </div>
                  <div class="col-md-6">
                    <p class="card-text">
                      {{ sustain_prop.value }} {{ sustain_prop.unit }}
                    </p>
                  </div>
                </div>
                <div class="col-md-12 material-page my-3">
                  <div class="d-grid gap-2">
                    <button
                      class="btn btn-success"
                      v-on:click="addToCart(article)"
                    >
                      Zum Warenkorb hinzufügen
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="text-center">
          <button
            class="btn btn-secondary btn-xl text-uppercase"
            v-on:click="backToSearch(false)"
          >
            Suche anpassen
          </button>
        </div>
      </div>
    </section>
    <EcoScoreModalComponent v-if="modalVisible" @close="closeModal">
      <template v-slot:header>
        <h5 class="modal-title">
          Wie berechnet sich der Eco-Score von
          {{ modalArticle.material.name }}?
        </h5>
      </template>
      <template v-slot:body>
        <div>
          <p>
            Der Eco-Score des Materials wird dynamisch berechnet. Dabei wird
            jedem Nachhaltigkeitskriterium einen eigenen Eco-Score zugewiesen,
            dieser berechnet sich für die einzelnen Kriterien wie folgt:
          </p>
          <hr />
          <p
            v-for="sustain_prob in modalArticle.material
              .sustainability_properties"
            :key="sustain_prob.id"
          >
            <span class="fw-bold">{{ sustain_prob.property_name }}</span> =
            <span
              >{{ sustain_prob.value }} {{ sustain_prob.unit }} =
              {{ sustain_prob.eco_score }}</span
            >
          </p>
          <hr />
          <p>
            Für {{ modalArticle.material.name }} ergibt sich dann ein Eco-Score
            von:
          </p>
          <p class="fw-bold">
            {{ modalArticle.material.name }}-Eco-Score: (
            <span
              v-for="(sustain_prob, index) in modalArticle.material
                .sustainability_properties"
              :key="index"
            >
              {{ sustain_prob.eco_score }}
              <span
                v-if="
                  index + 1 <
                  modalArticle.material.sustainability_properties.length
                "
                >+
              </span> </span
            >) / 4 = {{ modalArticle.ecological_index }}
          </p>
        </div>
      </template>
    </EcoScoreModalComponent>
    <BetterArticleModalComponent
      v-if="betterArticleModalVisible"
      @close="closeModal"
      @changeArticle="changeArticleOnModal(article)"
    >
      <template v-slot:header>
        <h5 class="modal-title">
          Es steht ein nachhaltigerer Artikel zur Verfügung!
        </h5>
      </template>
      <template v-slot:body>
        <p>Artikel <span class="fw-bold">{{ bestEcoScoreArticle.name }}</span> hat
        ähnliche von Ihnen gesuchte Eigenschaften mit einem besseren allgemeinen
        Eco-Score!</p>
        <p class="my-0">
          <span class="fw-bold">Materialstärke: </span>{{ bestEcoScoreArticle.depth }}mm
        </p>
        <p class="my-0">
          <span class="fw-bold">Maße: </span>{{ bestEcoScoreArticle.length }}mm x
          {{ bestEcoScoreArticle.width }}mm
        </p>
        <div
          class="row align-items-stretch"
          v-for="prop in bestEcoScoreArticle.material.properties"
          :key="prop.id"
        >
          <div class="col-md-6">
            <p class="card-text">{{ prop.property_name }}</p>
          </div>
          <div class="col-md-6">
            <p class="card-text">{{ prop.value }} {{ prop.unit }}</p>
          </div>
        </div>
        <hr />
        <div
          class="row align-items-stretch"
          v-for="sustain_prop in bestEcoScoreArticle.material.sustainability_properties"
          :key="sustain_prop.id"
        >
          <div class="col-md-6">
            <p class="card-text">{{ sustain_prop.property_name }}</p>
          </div>
          <div class="col-md-6">
            <p class="card-text">
              {{ sustain_prop.value }} {{ sustain_prop.unit }}
            </p>
          </div>
        </div>
      </template>
      <template v-slot:footer>
        <button
          class="btn btn-danger"
          v-on:click="changeArticleOnModal(bestEcoScoreArticle)"
        >
          Nicht Übernehmen
        </button>
        <button
          class="btn btn-success"
          v-on:click="changeArticleOnModal(bestEcoScoreArticle)"
        >
          Übernehmen
        </button>
      </template>
    </BetterArticleModalComponent>
  </div>
</template>

<script>
import EcoScoreModalComponent from "@/components/EcoScoreModalComponent.vue";
import BetterArticleModalComponent from "@/components/BetterArticleModalComponent.vue";
export default {
  name: "MaterialResultComponent",
  components: {
    EcoScoreModalComponent,
    BetterArticleModalComponent,
  },
  props: {
    articles: {
      type: Object,
      required: true,
    },
    sustainableArticle: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      bestArticle: {
        id: Number,
        name: String,
        description: String,
        material_class: String,
        depth: String,
        width: String,
        length: String,
        ecological_index: Number,
        material: {
          id: Number,
          properties: [],
          sustainability_properties: [],
        },
      },
      bestEcoScoreArticle: {},
      modalVisible: false,
      modalArticle: {},
      betterArticleModalVisible: false,
      betterArticleModalArticle: {},
    };
  },
  methods: {
    backToSearch(notReset) {
      this.$emit("change", notReset);
    },
    addToCart(article) {
      if (
        this.bestEcoScoreArticle.ecological_index < article.ecological_index
      ) {
        this.betterArticleModalVisible = true;
        this.betterArticleModalArticle = this.bestEcoScoreArticle;
      }
    },
    setBesArticle() {
      this.bestArticle = this.articles[0];
      this.bestEcoScoreArticle = this.articles[0];
      if (this.sustainableArticle) {
        for (const article of this.articles) {
          if (
            article.ecological_index < this.bestEcoScoreArticle.ecological_index
          ) {
            this.bestEcoScoreArticle = article;
          }
        }
      }
    },
    showModal(article) {
      this.modalArticle = article;
      this.modalVisible = true;
    },
    closeModal() {
      this.modalArticle = {};
      this.modalVisible = false;
      this.betterArticleModalVisible = false;
      this.betterArticleModalArticle = {};
    },
    changeArticleOnModal(article) {
      console.log(article);
      this.backToSearch(true);
      // // TODO: remove article from article list; set new Article to position one and go
      // this.bestArticle = article;
      this.betterArticleModalVisible = false;
      this.betterArticleModalArticle = {};
    },
  },
  created() {
    this.setBesArticle();
  },
};
</script>