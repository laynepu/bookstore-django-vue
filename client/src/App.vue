<script setup lang="ts">
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import { useCategoryStore } from "@/stores/CategoryStore";
const categoryStore = useCategoryStore();
categoryStore.fetchCategories();
</script>

<style></style>

<template>
  <div id="app">
    <!-- AppHeader, appHeader tag names also work, but it's strongly recommended using kebab inside DOM template in order to have syntax consistency with other html tags.-->
    <app-header></app-header>
    <router-view></router-view>
    <app-footer></app-footer>
  </div>
</template>
