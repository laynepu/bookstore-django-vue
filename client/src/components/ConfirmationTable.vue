<script setup lang="ts">
import { getBookImageUrl } from "@/utils";
import { useCartStore } from "@/stores/CartStore";
const cartStore = useCartStore();
import { asDollarsAndCents } from "@/utils";

import { useOrderDetailsStore } from "@/stores/OrderDetailsStore";
import { BookItem, OrderDetails } from "@/types";

const orderDetailsStore = useOrderDetailsStore();
const orderDetails: OrderDetails = orderDetailsStore.orderDetails;

// A helper function - optional to use
const bookAt = function (orderDetails: OrderDetails, index: number): BookItem {
  return orderDetails.books[index];
};
</script>

<style scoped>
.confirmation-table {
  display: grid;
  grid-template-columns: max-content minmax(10em, 15em) repeat(2, max-content);
  row-gap: 1em;
  width: fit-content;
  margin: 0 auto 1rem auto;
  padding-bottom: 1rem;
  background-color: var(--background-quinary-color);
}

ul {
  display: contents;
}

ul > li {
  display: contents;
}

.table-heading > * {
  background-color: var(--background-tertiary-color);
  padding: 0.5em;
}

.heading-book {
  grid-column: 1 / 3;
}

.heading-quantity {
  grid-column: 3;
  text-align: center;
}

.heading-subtotal {
  text-align: center;
  grid-column: -2 / -1;
}

.book-image {
  padding: 0 1em;
}

.book-image > * {
  margin-left: auto;
  margin-right: 0;
}

img {
  display: block;
  width: 30px;
  height: auto;
}

.book-title {
  display: flex;
  align-items: center;
}

.book-quantity {
  display: flex;
  align-items: center;
  justify-content: center;
}

.book-subtotal {
  display: flex;
  align-items: center;
  justify-content: center;
}

.book-quantity span {
  padding: 0 1rem;
}
</style>

<template>
  <div class="confirmation-table">
    <ul>
      <li class="table-heading">
        <div class="heading-book">Book</div>
        <div class="heading-quantity">Quantity</div>
        <div class="heading-subtotal">Amount</div>
      </li>

      <template
        v-for="(item, index) in orderDetails.lineItems"
        :key="item.bookId"
      >
        <li>
          <div class="book-image">
            <img 
              v-if="orderDetails.books && orderDetails.books[index]"
              :src="'/images/books/' + getBookImageUrl(orderDetails.books[index])" 
              :alt="orderDetails.books[index].title"
            />
          </div>
          <div class="book-title">
            {{ orderDetails.books[index].title }}
          </div>
          <div class="book-quantity">{{ item.quantity }}</div>
          <div class="book-subtotal">
            {{
              asDollarsAndCents(item.quantity * orderDetails.books[index].price)
            }}
          </div>
        </li>
      </template>
    </ul>
  </div>
</template>
