<script setup lang="ts">
import { useCartStore } from "@/stores/CartStore";
import { useCategoryStore } from "@/stores/CategoryStore";
const categoryStore = useCategoryStore();
const cartStore = useCartStore();
import { asDollarsAndCents, getBookImageUrl } from "@/utils";
</script>

<style scoped>
.cart-table {
  display: grid;
  grid-template-columns: max-content minmax(10em, 20em) repeat(3, max-content);
  row-gap: 1em;
  width: fit-content;
  margin: 0 auto 2rem auto;
  padding-bottom: 1rem;
  background-color: var(--background-quinary-color);
}

ul {
  display: contents;
}

ul > li {
  display: contents;
}

.table-heading {
  /*background-color: var(--background-tertiary-color);*/
  /*color: white;*/
}

.table-heading > * {
  background-color: var(--background-tertiary-color);
  padding: 0.5em;
}

.heading-book {
  grid-column: 1 / 3;
}

.heading-price {
  grid-column: 3;
  text-align: right;
}

.heading-quantity {
  grid-column: 4;
  text-align: center;
}

.heading-subtotal {
  text-align: right;
  grid-column: -2 / -1;
}

.cart-book-image {
  padding: 0 1em;
}

.cart-book-image > * {
  margin-left: auto;
  margin-right: 0;
}

img {
  display: block;
  width: 100px;
  height: auto;
}

.cart-book-price {
  text-align: center;
}

.cart-book-quantity {
  padding: 0 2rem;
}

.cart-book-subtotal {
  text-align: right;
  padding-left: 1em;
  padding-right: 1em;
}

/* Row separators in the table */

.line-sep {
  display: block;
  height: 2px;
  background-color: #837e7e;
  grid-column: 1 / -1;
}

/* Increment/decrement buttons */

.cart-book-quantity span {
  padding: 0 1rem;
}

.icon-button {
  border: none;
  cursor: pointer;
  background-color: var(--background-quinary-color);
}

.icon-button i {
  color: #fdba23;
  filter: brightness(95%);
}

.icon-button:hover > i {
  filter: brightness(105%);
}

.subtotal {
  padding-right: 1rem;
  padding-bottom: 1rem;
  grid-column: -3 / -1;
  text-align: right;
}

.clear-cart-btn {
  background-color: #f68363;
  color: #ffe1e1;
  border-radius: 0.2rem;
  box-shadow: 1px 1px grey;
  padding: 0.2rem 1rem;
  margin-left: 1rem;
}

.clear-cart-btn:hover {
  filter: brightness(0.95);
  color: white;
}

#cart-empty-div {
  text-align: center;
  padding: 2rem;
  margin-bottom: 5rem;
}

#cart-empty-div h2 {
  padding: 2rem;
  color: var(--tertiary-color);
}

.continue-shopping-link {
  background-color: var(--secondary-color);
  filter: drop-shadow(0.03rem 0.03rem 0.1rem rgb(160, 160, 160)) saturate(1.1);
}

.continue-shopping-link:hover {
  filter: saturate(1.05);
}

.checkout-div {
  text-align: center;
}

.checkout-link {
  background-color: var(--quinary-color);
  filter: drop-shadow(0.03rem 0.03rem 0.05rem rgb(160, 160, 160));
  margin-bottom: 2rem;
}

.checkout-link:hover {
  filter: brightness(1.05);
}
</style>

<template>
  <div v-if="!cartStore.cart.empty">
    <div class="cart-table">
      <ul>
        <li class="table-heading">
          <div class="heading-book">Book</div>
          <div class="heading-price">Price</div>
          <div class="heading-quantity">Quantity</div>
          <div class="heading-subtotal">Amount</div>
        </li>

        <template v-for="item in cartStore.cart.items" :key="item.book.bookId">
          <li>
            <div class="cart-book-image">
              <img
                :src="
                  '/images/books/' + getBookImageUrl(item.book)
                "
                :alt="item.book.title"
                width="100px"
                height="auto"
              />
            </div>
            <div class="cart-book-title">{{ item.book.title }}</div>
            <div class="cart-book-price">
              ${{ (item.book.price / 100).toFixed(2) }}
            </div>
            <div class="cart-book-quantity">
              <button
                class="icon-button inc-button"
                @click="
                  cartStore.updateBookQuantity(item.book, item.quantity + 1)
                "
              >
                <i class="fa-solid fa-circle-plus"></i>
              </button>
              <span class="quantity">{{ item.quantity }}</span>
              <button
                class="icon-button dec-button"
                @click="
                  cartStore.updateBookQuantity(item.book, item.quantity - 1)
                "
              >
                <i class="fa-solid fa-circle-minus"></i>
              </button>
            </div>
            <div class="cart-book-subtotal">
              {{ asDollarsAndCents(item.quantity * item.book.price) }}
            </div>
          </li>
        </template>
        <li class="line-sep"></li>
        <li>
          <div>
            <button
              class="clear-cart-btn button"
              @click="cartStore.clearCart()"
            >
              Clear Cart
            </button>
          </div>
          <div></div>
          <div></div>
          <div class="subtotal">
            Subtotal ({{ cartStore.count
            }}<span v-if="cartStore.count > 1"> Books</span>
            <span v-else> Book</span>):
            {{ asDollarsAndCents(cartStore.cart.subtotal) }}
          </div>
        </li>
      </ul>
    </div>
    <div class="checkout-div">
      <router-link
        :to="{
          name: 'category-view',
          params: { name: categoryStore.categoryName },
        }"
        class="button continue-shopping-link"
        >Continue Shopping</router-link
      >
      &nbsp;&nbsp;&nbsp;&nbsp;
      <router-link to="../Checkout/" class="button checkout-link"
        >Proceed to Checkout
      </router-link>
    </div>
  </div>
  <div v-else id="cart-empty-div">
    <h2>Your Cart is Empty</h2>
    <router-link
      :to="{
        name: 'category-view',
        params: { name: categoryStore.categoryName },
      }"
      class="button continue-shopping-link"
      >Continue Shopping</router-link
    >
  </div>
</template>
