<template>
  <div class="auth-error animate__animated animate__bounceIn">
    <i class="fa-solid fa-circle-xmark"></i>
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
import 'animate.css'
import { mapGetters } from 'vuex'

export default {
  name : 'AccountErrorList',
  computed : {
    ...mapGetters(['authError'])
  },
}
</script>

<style scoped lang='scss'>
.auth-error {
  width: 30rem;
  height: 4rem;
  background-color: $offwhiteColor;
  color: $adaptiveGrey800;
  font-size: 1.1rem;
  font-weight: bold;
  border-radius: 4px;
  position: fixed;
  left: calc(50vw - 15rem);
  bottom: 5vh;
  display: flex;
  padding: 0 2rem;
  justify-content: flex-start;
  align-items: center;
  z-index: 9999;
  filter: drop-shadow(0 0 2rem $warningColor);

  i {
    transform: translate(0, 10%);
    margin-right: 1rem;
  }
}
</style>