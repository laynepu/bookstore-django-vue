<script setup lang="ts">
import { useRoute } from "vue-router";
import { useCategoryStore } from "@/stores/CategoryStore";
const route = useRoute();
const categoryStore = useCategoryStore();
</script>

<style scoped>
#category-nav ul#category-buttons {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  flex-direction: row;
  text-align: center;
  background-color: var(--background-tertiary-color);
  padding: 0 1.5rem;
}

#category-nav .button {
  border-radius: 0;
  border-color: transparent;
}

.button.selected-category-button {
  background-color: var(--secondary-color);
}

.button.selected-category-button:hover {
  color: var(--quaternary-color);
}

.button.selected-category-button:active {
  filter: brightness(90%);
}

/* .button.unselected-category-button,
.button.unselected-category-button:visited {
  background-color: var(--background-tertiary-color);
} */

.button.unselected-category-button:hover {
  background-color: var(--background-tertiary-color);
  filter: brightness(95%);
  color: var(--quaternary-color);
}

.button.unselected-category-button:active {
  background-color: var(--background-tertiary-color);
  filter: brightness(85%);
}
</style>

<template>
  <nav id="category-nav">
    <ul id="category-buttons">
      <li
        v-for="category in categoryStore.categoryList"
        :key="category.categoryId"
      >
        <router-link
          :to="{ name: 'category-view', params: { name: category.name } }"
          class="button"
          :class="
            category.name === route.params.name
              ? 'selected-category-button'
              : 'unselected-category-button'
          "
        >
          {{ category.name }}
        </router-link>
      </li>
    </ul>
  </nav>
</template>
