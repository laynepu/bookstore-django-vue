<script setup lang="ts">
import { useCategoryStore } from "@/stores/CategoryStore";

const categoryStore = useCategoryStore();
// const headerDropdownOpen = ref(false);
// const toggleHeaderDropdown = function () {
//   headerDropdownOpen.value = !headerDropdownOpen.value;
// };
</script>

<style scoped>
#header-dropdown {
  position: relative;
}

#header-dropdown button {
  font-size: large;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--background-secondary-color);
}

#header-dropdown button:hover {
  filter: brightness(95%);
}

#header-dropdown i#dropdown-icon {
  padding-left: 0.5rem;
}

#header-dropdown ul {
  background-color: var(--background-quaternary-color);
  color: black;
  border-radius: 0.5rem;
  min-width: 8rem;
  position: absolute;
  z-index: 5;
  cursor: pointer;
  right: 0;
  visibility: hidden;
  filter: drop-shadow(0 0.03rem 0.05rem rgb(160, 160, 160));
  opacity: 0;
  transform: translateY(-1rem);
  transition: all 0.3s ease 0s;
  /*box-shadow: 1px 1px grey;*/
}

#header-dropdown li:first-child {
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
}

#header-dropdown li:last-child {
  border-bottom-left-radius: 0.5rem;
  border-bottom-right-radius: 0.5rem;
}

#header-dropdown a {
  color: black;
  text-decoration: none;
  width: 9rem;
  display: block;
  padding: 0.75rem 1rem;
}

#header-dropdown li:hover {
  background: var(--secondary-color);
}

#header-dropdown li:active {
  filter: brightness(95%);
}

/*#header-dropdown .header-dropdown-open {*/
/*  display: block;*/
/*}*/

#header-dropdown:hover ul,
#header-dropdown:focus ul {
  visibility: visible;
  transform: translateY(0);
  opacity: 1;
}
</style>

<template>
  <section id="header-category-section">
    <div id="header-dropdown" ref="root">
      <!--      <button class="button categories-button" @click="toggleHeaderDropdown">-->
      <button class="button categories-button">
        <span>Categories</span>
        <i id="dropdown-icon" class="fa-solid fa-angle-down"></i>
      </button>
      <!--      <ul :class="{ 'header-dropdown-open': headerDropdownOpen }">-->
      <ul>
        <li
          v-for="category in categoryStore.categoryList"
          :key="category.categoryId"
        >
          <router-link :to="'../category/' + category.name">
            {{ category.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </section>
</template>
