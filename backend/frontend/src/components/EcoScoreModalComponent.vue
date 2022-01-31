<template>
  <div class="modal-backdrop">
    <div class="modal">
      <div class="modal-content">
        <header class="modal-header">
          <slot name="header">
            This is the default title!
          </slot>
          <button type="button" class="btn-close" @click="close"></button>
        </header>

        <section class="modal-body">
          <slot name="body">
            This is the default body!
          </slot>
        </section>

        <!-- <footer class="modal-footer">
          <slot name="footer" class="modal-footer">
            This is the default footer!
          </slot>
        </footer> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EcoScoreModalComponent",
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>