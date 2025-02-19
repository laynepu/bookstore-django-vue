<script setup lang="ts">
import HeaderDropdown from "@/components/HeaderDropdown.vue";
import router from "../router";
import { useCartStore } from "@/stores/CartStore";
const cartStore = useCartStore();
const submitClick = function () {
  router.push("/category/Adventure");
};
</script>

<style scoped>
header {
  background: var(--background-secondary-color);
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
}

header #bookstore-logo-section {
  display: flex;
  align-items: center;
  padding-left: 1rem;
}

header a#header-logo-link {
  width: 4rem;
}

header a#header-logo-text-link {
  text-decoration: none;
}

header h1#header-text-logo {
  font-family: var(--default-font-family);
  text-align: left;
  padding: 0.5rem;
  color: var(--default-text-color);
}

header #search-bar-section {
  padding: 0 1rem;
}

header #search-bar-section form {
  display: flex;
  align-items: center;
  height: 2rem;
  width: 20rem;
}

header input[type="text"] {
  border-top-left-radius: 0.5rem;
  border-bottom-left-radius: 0.5rem;
  border: 0;
  height: 100%;
  padding: 1rem;
  width: 100%;
}

header input[type="submit"] {
  opacity: 60%;
  background: url("@/assets/images/site/magnifying-glass-solid.svg") no-repeat
    center;
  background-origin: content-box;
  background-color: white;
  padding: 3px;
  height: 100%;
  max-height: 100%;
  border: 0;
  border-top-right-radius: 0.5rem;
  border-bottom-right-radius: 0.5rem;
  width: 2.5rem;
  cursor: pointer;
}

header input[type="submit"]:hover {
  filter: brightness(90%);
}

header input[type="submit"]:active {
  filter: brightness(85%);
}

header a.button.cart-link {
  display: flex;
  align-items: center;
  background-color: var(--background-secondary-color);
  justify-content: space-between;
}

header a.button.cart-link:hover {
  filter: brightness(95%);
}

header i#cart-icon {
  font-size: x-large;
  padding-right: 0.5rem;
}

header a.button.sign-in-link {
  font-size: large;
  background-color: var(--background-secondary-color);
}

header a.button.sign-in-link:hover {
  filter: brightness(95%);
}
</style>

<template>
  <header class="container">
    <section id="bookstore-logo-section">
      <router-link to="/" id="header-logo-link">
        <img
          src="@/assets/images/site/pepe-store-logo.gif"
          alt="Pepe's Bookstore Logo"
        />
        <!-- @ is a path alias for the src directory -->
      </router-link>
      <router-link to="/" id="header-logo-text-link">
        <h1 id="header-text-logo">Pepe's Bookstore</h1>
      </router-link>
    </section>
    <section id="search-bar-section">
      <form @submit.prevent="submitClick">
        <input type="text" placeholder="Find a book" />
        <input type="submit" value=" " />
      </form>
    </section>
    <section id="header-category-section">
      <header-dropdown></header-dropdown>
    </section>
    <section id="header-cart-section">
      <router-link to="../Cart/" class="button cart-link"
        ><i id="cart-icon" class="fa-solid fa-cart-shopping"></i>
        <p>{{ cartStore.count }}</p></router-link
      >
    </section>
    <router-link to="#" class="button sign-in-link">Login</router-link>
  </header>
</template>
