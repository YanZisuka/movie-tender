<template>
  <div class="index">
    <video muted autoplay loop>
      <source :src="bgVideo" type="video/mp4" />
    </video>

    <div class="d-flex flex-column justify-content-center text-center">
      <h1>movietender</h1>
      <p>지금,</p>
      <p class="mb-4">어떤 영화를 볼지 고민된다면?</p>
      <button
        v-if="!isLoggedIn"
        @click="switchShowAccountModal()"
        class="button"
      >
        로그인
      </button>
      <router-link
        v-else
        :to="{ name: 'logout', params: { username: currentUser.username } }"
      >
        <button class="button">로그아웃</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "IndexView",

  data() {
    return {
      bgVideo: require("@/assets/bg-video.mp4"),
    };
  },

  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
  },

  methods: {
    ...mapActions(["switchShowAccountModal"]),
  },

  created() {
    document.body.style.backgroundColor = "#171717";
    this.$emit("dark-emit");
  },
};
</script>

<style scoped lang="scss">
.index {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 85px);

  video {
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: -1;
    filter: brightness(40%);
  }
  h1 {
    font-family: "Lobster", cursive;
    font-size: 4rem;
    font-weight: 700;
    color: $whiteColor;
  }
  p {
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.5;
    margin: 0;
    color: $whiteColor;
  }
}
</style>
