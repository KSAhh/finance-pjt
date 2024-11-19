<template>
  <button
    @click="goToLogin"
    class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 whitespace-nowrap"
  >
    로그인
  </button>
</template>

<script>
export default {
  name: "LoginButton",
  methods: {
    goToLogin() {
      this.$router.push({ name: "LoginView" }); // LoginView로 이동
    },
  },
};
</script>
