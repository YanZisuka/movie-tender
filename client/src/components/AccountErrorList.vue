<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in authError" :key="field" >
      <!-- {{ field }} -->
      <ul>
      <p v-for="(error, idx) in errors" :key="idx">{{ error }}</p>
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
    color: #cf1224;
    font-size: 25px;
  }
</style>