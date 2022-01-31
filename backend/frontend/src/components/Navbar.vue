<template>
  <!-- Navigation-->
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
    <div class="container">
      <!-- <a class="navbar-brand" href="#page-top"><img src="@/assets/img/resolve-logo.svg" alt="..." /></a> -->
      <router-link class="navbar-brand" :to="{ name: 'home' }">
        <span class="logo-first">re</span>
        <span class="logo-middle">:</span>
        <span class="logo-end">solve</span>
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarResponsive"
        aria-controls="navbarResponsive"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        Menu
        <i class="fas fa-bars ms-1"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav text-uppercase ms-auto py-4 py-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'compareMaterial' }">Materialien vergleichen</router-link>
          </li>
          <li class="nav-item">
           <a class="nav-link" href="#about">Über Uns</a>
          </li>
          <li class="nav-item">
           <a class="nav-link" href="#ecoscore">Eco Score</a>
          </li>
          <!-- <li class="nav-item">
            <a class="nav-link" href="#portfolio">Portfolio</a>
          </li> -->
          <li class="nav-item"><a class="nav-link" href="#team">Team</a></li>
          <li class="nav-item">
            <a class="nav-link" href="#contact">Kontaktiere uns</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
  mounted() {
      this.$nextTick(function(){
        window.addEventListener("scroll", function(){
          const navbarCollapsible = document.body.querySelector('#mainNav');
          if (!navbarCollapsible) {
              return;
          }
          if (window.scrollY === 0) {
              navbarCollapsible.classList.remove('navbar-shrink')
          } else {
              navbarCollapsible.classList.add('navbar-shrink')
          }
          
          // // Activate Bootstrap scrollspy on the main nav element
          // const mainNav = document.body.querySelector('#mainNav');
          // if (mainNav) {
          //   this.$('body').scrollspy({ target: '#navbar-example', offset: 74, })
          // }
        })

      })
    },
};
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #dddddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 150%;
}
.logo-first {
  /* font-family:"aristotelica-pro-display-extralight"; */
  text-transform: lowercase; 
  color: #009600;
}
.logo-middle {
  /* font-family:"aristotelica-pro-display-extralight"; */
  text-transform: lowercase; 
  color: grey;
}
.logo-end {
  /* font-family:"aristotelica-pro-display-extralight"; */
  text-transform: lowercase; 
  color: #054263;
}
</style>