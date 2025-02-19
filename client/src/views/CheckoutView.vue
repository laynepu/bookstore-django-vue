<script setup lang="ts">
import { reactive } from "vue";
import useVuelidate from "@vuelidate/core";
import { helpers, required } from "@vuelidate/validators";
import { useCartStore } from "@/stores/CartStore";
const cartStore = useCartStore();
const cart = cartStore.cart;
import { isCreditCard, isMobilePhone, isEmailAddress } from "@/utils";
import CheckoutFieldError from "@/components/CheckoutFieldError.vue";
import { asDollarsAndCents } from "@/utils";
import { useCategoryStore } from "@/stores/CategoryStore";
const categoryStore = useCategoryStore();
import router from "@/router";

const months: string[] = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

let years: number[] = [];
for (let i = 0; i < 16; i++) {
  years.push(yearFrom(i));
}

const form = reactive({
  name: "",
  address: "",
  phone: "",
  email: "",
  ccNumber: "",
  ccExpiryMonth: new Date().getMonth() + 1,
  ccExpiryYear: new Date().getFullYear(),
  checkoutStatus: "",
});

const rules = {
  name: {
    required: helpers.withMessage("Please provide a name.", required),
    minLength: helpers.withMessage(
      "Name must have at least 4 letters.",
      (value: string) => !helpers.req(value.trim()) || value.trim().length >= 4
    ),
    maxLength: helpers.withMessage(
      "Name can have at most 45 letters.",
      (value: string) => !helpers.req(value.trim()) || value.trim().length <= 45
    ),
  },
  phone: {
    required: helpers.withMessage("Please provide a phone number.", required),
    phone: helpers.withMessage(
      "The phone number is invalid.",
      (value: string) =>
        !helpers.req(value.trim()) || isMobilePhone(value.trim())
    ),
  },
  address: {
    required: helpers.withMessage(
      "Please provide a mailing address.",
      required
    ),
    minLength: helpers.withMessage(
      "Address must have at least 4 letters.",
      (value: string) => !helpers.req(value.trim()) || value.trim().length >= 4
    ),
    maxLength: helpers.withMessage(
      "Address can have at most 45 letters.",
      (value: string) => !helpers.req(value.trim()) || value.trim().length <= 45
    ),
  },
  email: {
    required: helpers.withMessage("Please provide an email address.", required),
    phone: helpers.withMessage(
      "The Email address is invalid.",
      (value: string) =>
        !helpers.req(value.trim()) || isEmailAddress(value.trim())
    ),
  },
  ccNumber: {
    required: helpers.withMessage(
      "Please provide a credit card number.",
      required
    ),
    ccNumber: helpers.withMessage(
      "The credit card number is invalid.",
      (value: string) =>
        !helpers.req(value.trim()) || isCreditCard(value.trim())
    ),
  },
  ccExpiryMonth: {
    required: helpers.withMessage(
      "Please select the month of the expiry date.",
      required
    ),
  },
  ccExpiryYear: {
    required: helpers.withMessage("Please select the expiry year.", required),
  },
};
const $v = useVuelidate(rules, form);

async function submitOrder() {
  console.log("Submit order");
  const isFormCorrect = await $v.value.$validate();
  if (!isFormCorrect) {
    form.checkoutStatus = "ERROR";
  } else {
    form.checkoutStatus = "PENDING";
    await cartStore
      .placeOrder({
        name: form.name,
        address: form.address,
        phone: form.phone,
        email: form.email,
        ccNumber: form.ccNumber,
        ccExpiryMonth: form.ccExpiryMonth,
        ccExpiryYear: form.ccExpiryYear,
      })
      .then(() => {
        form.checkoutStatus = "OK";
        cartStore.clearCart();
        router.push({ name: "confirmation-view" });
      })
      .catch((reason) => {
        form.checkoutStatus = "SERVER_ERROR";
        console.log("Error placing order", reason);
      });
  }
}

/* NOTE: For example yearFrom(0) == <current_year> */
function yearFrom(index: number) {
  return new Date().getFullYear() + index;
}
</script>

<style scoped>
.checkout-page {
  background: var(--background-primary-color);
}

.page-title {
  padding: 2rem 0;
  text-align: center;
}

.checkout-page-body {
  padding-bottom: 5rem;
  padding-top: 2rem;
  margin: 0 10%;
}

form {
  display: flex;
  justify-content: space-around;
  width: 100%;
  background-color: var(--background-quaternary-color);
  border-radius: 0.5rem;
  padding: 1rem;
}

form .payment-info {
  display: flex;
  flex-direction: column;
}

.payment-info > div {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin: 0.5rem 0;
}

.payment-info > div input,
.payment-info > div select {
  background-color: white;
  margin-left: 0.5em;
  border: 0;
  border-radius: 0.3rem;
  padding: 2px 6px;
  width: 200px;
}

#address-input-text2 {
  margin: 0 0 0.5rem 0;
}

.payment-info > div select#month {
  width: 120px;
}

.payment-info > div select#year {
  width: 72px;
}

.checkout-summary {
  display: flex;
  flex-direction: column;
}

.checkout-summary-title {
  padding-top: 0.5rem;
  padding-bottom: 1.5rem;
}

.checkout-summary > div {
  display: flex;
  justify-content: space-between;
  padding: 0.2rem 0;
}

.total-charge span {
  font-size: large;
  padding: 1rem 0;
}

.checkout-button {
  background-color: var(--quinary-color);
  filter: drop-shadow(0.03rem 0.03rem 0.05rem rgb(160, 160, 160));
}

.checkout-button:hover {
  filter: brightness(1.05);
}

.checkoutStatusBox {
  text-align: left;
  padding: 2rem 0;
}

.status-error-msg {
  color: var(--tertiary-color);
}

.continue-shopping-link {
  background-color: var(--secondary-color);
  filter: drop-shadow(0.03rem 0.03rem 0.1rem rgb(160, 160, 160)) saturate(1.1);
}

.continue-shopping-link:hover {
  filter: saturate(1.05);
}

.empty-checkout {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  margin-bottom: 6rem;
}

.empty-hint {
  padding: 2rem 0;
  text-align: center;
}

.empty-hint > h2 {
  color: var(--tertiary-color);
  padding-bottom: 1rem;
}
</style>

<template>
  <div class="checkout-page">
    <h1 class="page-title">Checkout</h1>
    <section class="checkout-page-body" v-if="!cart.empty">
      <form @submit.prevent="submitOrder" id="checkout-form">
        <div class="payment-info">
          <div>
            <label for="name">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              v-model.lazy="$v.name.$model"
            />
          </div>
          <CheckoutFieldError field-name="name" :validator="$v" />

          <div>
            <label for="address">Address</label>
            <div class="address-input-text">
              <input
                type="text"
                class="address"
                name="address1"
                v-model.lazy="$v.address.$model"
              />
            </div>
          </div>
          <div id="address-input-text2">
            <input type="text" class="address" name="address2" />
          </div>
          <CheckoutFieldError field-name="address" :validator="$v" />

          <div>
            <label for="phone">Phone</label>
            <input
              class="textField"
              type="text"
              id="phone"
              name="phone"
              v-model.lazy="$v.phone.$model"
            />
          </div>
          <CheckoutFieldError field-name="phone" :validator="$v" />

          <div>
            <label for="email">Email</label>
            <input
              type="text"
              id="email"
              name="email"
              v-model.lazy="$v.email.$model"
            />
          </div>
          <CheckoutFieldError field-name="email" :validator="$v" />

          <div>
            <label for="ccNumber">Credit card</label>
            <input
              type="text"
              id="ccNumber"
              name="ccNumber"
              v-model.lazy="$v.ccNumber.$model"
            />
          </div>
          <CheckoutFieldError field-name="ccNumber" :validator="$v" />

          <div>
            <label>Exp Date</label>
            <select v-model="$v.ccExpiryMonth.$model" id="month">
              <option
                v-for="(month, index) in months"
                :key="index"
                :value="index + 1"
              >
                {{ month }}
              </option>
            </select>
            <select v-model="$v.ccExpiryYear.$model" id="year">
              <option v-for="(year, index) in years" :key="index">
                {{ year }}
              </option>
            </select>
          </div>
        </div>

        <div class="checkout-summary">
          <h2 class="checkout-summary-title">Purchase Summary</h2>
          <div>
            <span v-if="cartStore.count > 1"
              >Subtotal ({{ cartStore.count }} items)</span
            >
            <span v-else>Subtotal ({{ cartStore.count }} item)</span>
            <span>{{ asDollarsAndCents(cart.subtotal) }}</span>
          </div>

          <div>
            <span>Shipping</span>
            <span>{{ asDollarsAndCents(cart.surcharge) }}</span>
          </div>

          <div class="total-charge">
            <span>Total</span>
            <span>{{ asDollarsAndCents(cart.subtotal + cart.surcharge) }}</span>
          </div>

          <input
            type="submit"
            name="submit"
            class="button checkout-button"
            :disabled="form.checkoutStatus === 'PENDING'"
            value="Complete Purchase"
          />
          <section
            v-show="form.checkoutStatus !== ''"
            class="checkoutStatusBox"
          >
            <div v-if="form.checkoutStatus === 'ERROR'">
              Error: Please fix the problems<br />specified in red.
            </div>

            <div v-else-if="form.checkoutStatus === 'PENDING'">
              Processing...
            </div>

            <div v-else-if="form.checkoutStatus === 'OK'">Order placed...</div>

            <div class="status-error-msg" v-else>
              An unexpected error occurred,<br />please try again.
            </div>
          </section>
        </div>
      </form>
    </section>
    <div v-else class="empty-checkout">
      <div class="empty-hint">
        <h2>Your Cart is Empty.</h2>
        <h2>Please Fill Your Cart Before Checkout.</h2>
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
  </div>
</template>
