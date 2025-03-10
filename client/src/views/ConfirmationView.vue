<script setup lang="ts">
import { useOrderDetailsStore } from "@/stores/OrderDetailsStore";
import { computed } from "vue";
import ConfirmationTable from "@/components/ConfirmationTable.vue";
import { useCartStore } from "@/stores/CartStore";
import { useCategoryStore } from "@/stores/CategoryStore";
import { asDollarsAndCents } from "@/utils";
const categoryStore = useCategoryStore();
const cartStore = useCartStore();

const orderDetailsStore = useOrderDetailsStore();
const orderDetails = orderDetailsStore.orderDetails;

const orderDate = computed(function () {
  let date = new Date(orderDetails.order.dateCreated);
  return date.toLocaleTimeString();
});

const ccExpDate = computed(function (): Date {
  return new Date(orderDetails.customer.ccExpDate);
});

const ccExpYear = computed(function (): number {
  return ccExpDate.value.getFullYear();
});

const ccExpMonth = computed(function (): string {
  let month = ccExpDate.value.getMonth() + 1;
  let result = "" + month;
  if (month < 10) {
    result = "0" + month;
  }
  return result;
});
</script>

<style scoped>
h1 {
  margin: 1em auto;
  text-align: center;
}

#confirmationView {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2rem auto;
}

ul {
  text-align: left;
}

ul > li {
  margin: 0.25em;
}

h3 {
  padding: 1rem 0 0.5rem 0;
  color: #be4c4c;
}

#customerInfo .label {
  display: inline-block;
  width: 10rem;
  font-weight: bold;
  text-align: end;
}

#customerInfo .value {
  display: inline-block;
  width: 15rem;
  margin-left: 1rem;
  text-align: start;
}

.subtotal-outer-div {
  display: flex;
  width: 28rem;
  justify-content: right;
  padding-bottom: 1rem;
}

.subtotal {
  padding: 0 1rem;
  width: 15rem;
  text-align: right;
}

.subtotal > div {
  display: flex;
  justify-content: space-between;
  padding: 0.2rem 0;
}

.total-charge span {
  font-size: large;
  font-weight: bold;
}

.continue-shopping-link {
  background-color: var(--secondary-color);
  filter: drop-shadow(0.03rem 0.03rem 0.1rem rgb(160, 160, 160)) saturate(1.1);
}

.continue-shopping-link:hover {
  filter: saturate(1.05);
}

#noDetails {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  margin-bottom: 6rem;
}

.home-page-link {
  background-color: var(--secondary-color);
  filter: drop-shadow(0.03rem 0.03rem 0.1rem rgb(160, 160, 160)) saturate(1.1);
}

.home-page-link:hover {
  filter: saturate(1.05);
}

#noDetails p {
  font-size: large;
  padding-bottom: 2rem;
}
</style>

<template>
  <h1>Order Details</h1>
  <div id="noDetails" v-if="!orderDetailsStore.hasOrderDetails()">
    <p>We are sorry, the order you requested could not be found.</p>
    <router-link class="button home-page-link" :to="{ name: 'home-view' }">
      Go to Home Page
    </router-link>
  </div>
  <div id="confirmationView" v-else>
    <ul>
      <li>Confirmation #: {{ orderDetails.order.confirmationNumber }}</li>
      <li>
        Time:
        {{ new Date(orderDetails.order.dateCreated).toLocaleString() }}
      </li>
    </ul>
    <h3>---------------------- Your Information ----------------------</h3>
    <div id="customerInfo">
      <ul>
        <li>
          <span class="label">Name</span
          ><span class="value">{{ orderDetails.customer.name }}</span>
        </li>
        <li>
          <span class="label">Address</span
          ><span class="value">{{ orderDetails.customer.address }}</span>
        </li>
        <li>
          <span class="label">Email</span
          ><span class="value">{{ orderDetails.customer.email }}</span>
        </li>
        <li>
          <span class="label">Phone</span
          ><span class="value">{{ orderDetails.customer.phone }}</span>
        </li>
        <li>
          <span class="label">Credit Card</span
          ><span class="value"
            >
            {{ orderDetails.customer.maskedCCNumber }}
            (exp. {{ orderDetails.customer.ccExpDate.substring(5, 7) }}/{{
              orderDetails.customer.ccExpDate.substring(0, 4)
            }})</span
          >
        </li>
      </ul>
    </div>
    <h3>----------------------- Ordered Books -----------------------</h3>
    <confirmation-table> </confirmation-table>
    <div class="subtotal-outer-div">
      <div class="subtotal">
        <div>
          <span v-if="cartStore.count > 1"
            >Subtotal ({{ cartStore.count }} items)</span
          >
          <span v-else>Subtotal ({{ cartStore.count }} item)</span>
          <span>{{
            asDollarsAndCents(
              orderDetails.order.amount - cartStore.cart.surcharge
            )
          }}</span>
        </div>

        <div>
          <span>Shipping</span>
          <span>{{ asDollarsAndCents(cartStore.cart.surcharge) }}</span>
        </div>

        <div class="total-charge">
          <span>Total</span>
          <span>{{ asDollarsAndCents(orderDetails.order.amount) }}</span>
        </div>
      </div>
    </div>
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
