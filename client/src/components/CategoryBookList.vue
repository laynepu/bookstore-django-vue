<script setup lang="ts">
import { useBookStore } from "@/stores/BookStore";
import CategoryBookListItem from "@/components/CategoryBookListItem.vue";
const bookStore = useBookStore();
</script>

<style scoped>
#book-boxes {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(21rem, 1fr));
  justify-content: space-around;
  grid-gap: 0.5rem;
  padding: 1rem 1rem;
}
</style>

<template>
  <section id="category-book-list">
    <ul id="book-boxes">
      <li v-for="book in bookStore.bookList" :key="book.bookId">
        <category-book-list-item :book="book"></category-book-list-item>
      </li>
    </ul>
  </section>
</template>
