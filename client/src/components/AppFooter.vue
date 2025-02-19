<script setup lang="ts"></script>

<style scoped>
footer {
  background: var(--background-tertiary-color);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}

footer section {
  display: flex;
}

footer > :first-child,
footer > :last-child {
  flex-grow: 1;
  flex-basis: 0;
}

footer > * {
  padding: 0 1rem;
}

footer section#links {
  display: flex;
  align-items: center;
}

footer section#links a {
  padding: 0.5rem 0.1rem;
}

footer section#links a:hover,
a:active {
  color: var(--quaternary-color);
}

footer section#links span {
  padding: 0 0.5rem;
}

footer section#social-media-icons i {
  font-size: 1.7em;
}

footer section#social-media-icons .button:hover {
  background-color: var(--background-tertiary-color);
  filter: brightness(95%);
}

footer > span {
  display: inline-block;
  text-align: end;
}
</style>

<template>
  <footer class="container">
    <section id="links">
      <router-link to="/">About</router-link>
      <span>|</span>
      <router-link to="/">Contact</router-link>
      <span>|</span>
      <router-link to="/">Directions</router-link>
    </section>
    <section id="social-media-icons">
      <router-link to="/" class="button"
        ><i class="fa-brands fa-facebook"></i
      ></router-link>
      <router-link to="/" class="button"
        ><i class="fa-brands fa-instagram"></i
      ></router-link>
      <router-link to="/" class="button"
        ><i class="fa-brands fa-twitter"></i
      ></router-link>
    </section>
    <span>Copyright © 2022 Pepe's Bookstore</span>
  </footer>
</template>
