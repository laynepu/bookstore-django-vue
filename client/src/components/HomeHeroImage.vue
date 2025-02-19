<template>
  <section id="hero-section">
    <img id="hero-img" src="@/assets/images/site/hero-img.png" alt="hero-img" />

    <!--    option 1-->
    <!--    <router-link to="../category/horror" id="call-to-action-btn" class="button"-->
    <!--      >SHOP FOR BOOKS</router-link-->
    <!--    >-->

    <!--    option 2-->
    <router-link
      :to="{ name: 'category-view', params: { name: 'Adventure' } }"
      id="call-to-action-btn"
      class="button"
      >SHOP FOR BOOKS</router-link
    >
  </section>
</template>

<script setup lang="ts"></script>

<style scoped>
div#main-content section#hero-section {
  position: relative;
}

div#main-content img#hero-img {
  filter: saturate(120%) contrast(120%);
}

div#main-content a#call-to-action-btn {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: min(2vw, 1rem) min(3vw, 2.5rem);
  border: none;
  box-shadow: 1px 1px grey;
  border-radius: 1rem;
  background-color: rgb(254, 203, 74);
  font-weight: bold;
  font-size: min(2vw, 20px);
  transition: all 0.1s linear 0s;
}

div#main-content a#call-to-action-btn:hover {
  transform: translate(-50%, -50%) scale(1.15);
  /*font-size: min(2vw, 20px) * 1.1;*/
  filter: brightness(105%);
}

div#main-content a#call-to-action-btn:active {
  color: var(--default-text-color);
  filter: brightness(100%);
}
</style>
