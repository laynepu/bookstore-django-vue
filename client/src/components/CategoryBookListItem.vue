<template>
  <li class="book-box">
    <div class="book-img" :class="book.isPublic ? 'read-now-available' : null">
      <img
        :src="require('@/assets/images/books/' + getBookImageUrl(book))"
        :alt="book.title"
      />
      <router-link to="#" v-if="book.isPublic">Read now</router-link>
    </div>
    <div class="book-info">
      <div class="title-author">
        <div class="book-title">{{ book.title }}</div>
        <div class="book-author">{{ book.author }}</div>
      </div>
      <div class="price-addToCart-button">
        <div class="book-price">{{ asDollarsAndCents(book.price) }}</div>
        <button
          class="button add-to-cart-button"
          @click="cartStore.addToCart(book)"
        >
          Add to Cart
        </button>
      </div>
    </div>
  </li>
</template>

<script setup lang="ts">
import { defineProps } from "vue";
import { BookItem } from "@/types";
import { useCartStore } from "@/stores/CartStore";
const cartStore = useCartStore();
import { asDollarsAndCents, getBookImageUrl } from "@/utils";

defineProps<{
  book: BookItem;
}>(); // type-based declaration
</script>

<style scoped>
.book-box {
  display: flex;
  background-color: var(--background-quinary-color);
  height: calc(200px + 2rem);
  padding: 1rem;
}

.book-img {
  position: relative;
  height: 100%;
  width: 50%;
}

#category-book-list .book-img img {
  margin: auto;
  height: 100%;
}

#category-book-list .book-img.read-now-available img {
  filter: brightness(60%);
}

#category-book-list .book-img.read-now-available a {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 0.1rem 0.2rem;
  border-radius: 1rem;
  border: solid 1px #ffffff;
  text-align: center;
  color: #ffffff;
  width: 6rem;
}

#category-book-list .book-img.read-now-available a:hover {
  filter: brightness(90%);
}

.book-info {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0.5rem 0 0.5rem 0.2rem;
  width: 50%;
}

.book-title {
  font-weight: bold;
}

.book-author {
  font-style: italic;
  padding-top: 0.5rem;
}

.book-price {
  color: rgb(208, 0, 0);
  padding-bottom: 1rem;
}

.add-to-cart-button {
  width: 100%;
  background-color: var(--quinary-color);
  filter: drop-shadow(0.03rem 0.03rem 0.1rem rgb(160, 160, 160));
}

#category-book-list .add-to-cart-button:hover {
  filter: brightness(105%)
    drop-shadow(0.03rem 0.03rem 0.05rem rgb(160, 160, 160));
}

#category-book-list .add-to-cart-button:active {
  filter: brightness(100%);
}
</style>
