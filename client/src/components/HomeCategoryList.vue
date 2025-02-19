<script setup lang="ts">
import { inject } from "vue";
import { CategoryItem } from "@/types";
const categoryList = inject("categoryList");
const categoryImageFileName = function (category: CategoryItem): string {
  let name = category.name.toLowerCase();
  name = name.replace(/ /g, "-");
  name = name.replace(/'/g, "");
  return `${name}.jpg`;
};
</script>

<style scoped>
ul {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 1em;
}

li {
  text-align: center;
  cursor: pointer;
}

li div {
  padding: 0.5em 0;
  background: rgba(0, 0, 0, 0.5); /* last # is percent opacity */
  color: white;
  transform: translateY(-2.25em);
  margin-bottom: -2em;
}
</style>

<template>
  <ul>
    <li v-for="category in categoryList" :key="category.categoryId">
      <router-link :to="'../category/' + category.name">
        <img
          :src="
            require('@/assets/images/categories/' +
              categoryImageFileName(category))
          "
          :alt="category.name + 'category'"
        />
        <div>{{ category.name }}</div>
      </router-link>
    </li>
  </ul>
</template>
