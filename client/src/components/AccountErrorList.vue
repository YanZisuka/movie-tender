<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in authError" :key="field" >
      <!-- {{ field }} -->
      <ul class="m-0 p-0">
        <li>
          <p v-for="(error, idx) in errors" :key="idx">{{ error }}</p>
        </li>
      </ul>
    </p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name : 'AccountErrorList',
  computed : {
    ...mapGetters(['authError'])
  },
}
</script>

<style>
  .account-error-list {
    width: 100%;
    color: #db2828;
    font-size: 1rem;
  }

  .account-error-list li {
    list-style: none;
  }
</style>