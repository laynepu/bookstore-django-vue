<script setup lang="ts">
import CartTable from "@/components/CartTable.vue";
import { useCartStore } from "@/stores/CartStore";
const cartStore = useCartStore();
const clearCart = function () {
  cartStore.cart.clear();
};
</script>
<style scoped>
h1 {
  margin: 1em auto;
  text-align: center;
}
</style>

<template>
  <h1>Your Cart</h1>
  <cart-table></cart-table>
</template>
