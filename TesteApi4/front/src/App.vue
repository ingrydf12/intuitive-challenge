<script setup>
import About from './components/About.vue'
import './assets/main.css';
import SearchView from './views/SearchView.vue';

</script>

<template>
  <header>
    <img alt="Computer logo" class="logo" src="@/assets/outline-pc.gif" width="250" height="200" />

    <div class="wrapper">
      <About msg="Interactive API" />
    </div>
  </header>
<main> 
  <SearchView />
</main>
 
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  padding-top: 5rem;
}

main{
  padding-top: 5rem;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}


@media (min-width: 1024px) {
  header {
    display: flex;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
