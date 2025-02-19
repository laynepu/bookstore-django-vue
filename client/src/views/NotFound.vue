<template>
  <div class="page-not-found">
    <h1>Your Content was Not Found</h1>
    <p>There appears to be nothing to find here.</p>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.page-not-found {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  margin-bottom: 6rem;
}

.page-not-found > * {
  padding: 1rem 0;
}

h1 {
  color: var(--tertiary-color);
}

p {
  font-size: large;
}
</style>
