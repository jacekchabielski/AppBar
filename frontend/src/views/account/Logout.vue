<template></template>

<script>
export default {
  name: "Logout",
  data() {
    return {};
  },
  mounted() {
    this.logout();
  },
  methods: {
    async logout() {
      this.$store.commit({
        type: "logoutUser",
      });
      window.location.href = "/";
    },
  },
};
</script>
