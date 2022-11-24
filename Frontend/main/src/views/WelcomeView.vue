<template>
  <div class="logo_center">
    <router-link to="/">
        <img class="logo_center" src="@/assets/logo.svg">
    </router-link>
    <h1>Mentor's Portal</h1>
    <h2>Indian Institute of Technology, Madras</h2>
    <h3>BS Degree in Data Science and Applications</h3>
    <p>New User?</p>
    <router-link to="/register" >
      <button value="Register">Register</button>
    </router-link>
    <p>or</p>
    <router-link to="/login">
      <button value="Login">Login</button>
    </router-link>
  </div>
</template>

<script>
export default {
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.logo_center{
  /* border: 1px solid black; */
  justify-content: center;
  height: 100%;
}
.logo_center img{
  /* border: 1px solid black; */
  margin: 4% 0 0 0;
  width: 300px;
}
.logo_center button{
  background-color: #ff7b00ab;
  border: none;
  font-size: 90%;
  border-radius: 25px;
  width:auto;
  padding: 0 20px 0 20px;
  height: 40px;
}
.logo_center button[value=Login]{
  background-color: rgba(4, 255, 67, 0.69);
}
button:hover{
  box-shadow: 0 12px 16px 0 rgba(136, 135, 135, 0.625)}
</style>
