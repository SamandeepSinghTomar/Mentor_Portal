<template>
  <div class="container">
    <div class="row">
      <div class="arrow_column">
        <button href="#" style="text-decoration:none;color:white;" @click="$router.go('-1')">&lt;</button>
      </div>
    <div class="column">
      <router-link to="/">
        <img class="logo_center" src="@/assets/logo.svg">
      </router-link>
      <p style="font-style:italic;">Not a User? <router-link to="/register" style="color:#ff7b00;text-decoration: none;">Register</router-link></p>
    </div>
    <div class="column register">
      <form action="#">
      <input type="text" id="user_name" name="user_name" placeholder="User name" v-model="user_name"><br>
      <input type="password" id="password" name="password" placeholder="Password" v-model="password"><br>
      <button id="submit" name="submit" value="Login" @click="login()">Login</button>
      </form>
    </div>
  </div>
</div>
</template>

<script>
export default {
  data(){
    return{
      user_name: "",
      password: "",
    }
  },
  methods: {
    async login() {
       {
        const requestOptions = {
          method: "GET",
          headers: { "Content-Type": "application/json"},
          credentials: 'include',
        };
        const response = await fetch(this.$store.state.BaseURL+"/user/"+this.user_name+"/"+this.password, requestOptions);
        let fields = await response.json()
        localStorage.token =await fields['token'];
        localStorage.user_name =await fields['user_name'];
        localStorage.first_name =await fields['first_name'];
        localStorage.middle_name =await fields['middle_name'];
        localStorage.last_name =await fields['last_name'];
        localStorage.user_id =await fields['user_id'];
        localStorage.dob =await fields['dob'];
        localStorage.email =await fields['email'];
        localStorage.roll_number =await fields['roll_number'];
        localStorage.role =await fields['role'];
        localStorage.created_at =await fields['created_at'];
        this.$router.push({ path: '/dashboard' });
      }
    },
  },
  beforeMount() {
    // this.$router.push('/login')
  },
}
</script>


<style scoped>
* {
box-sizing: border-box;
}
.row{
overflow: hidden;
width:70%;
margin:6em auto 0 auto;
border-radius: 50px;
box-shadow: 10px 12px 16px 0 rgba(136, 135, 135, 0.625);
}
.column {
/* border:1px solid black; */
float: left;
width: 50%;
padding: 5% 0 5% 0;
margin: 0 0 5% 0;
/* height: 300px; Should be removed. Only for demonstration */
}
.arrow_column button{
  width:100%;display: flex;justify-content: flex-start;
  text-decoration: none;
  font-size: 35px;
  margin: 20px 0 0 20px;
  padding:0 0 0 9px;
  content: "";
  width: 40px;
  height: 40px;
  border-radius: 20px;
  color: white;
  border:0;
  background-color: rgba(4, 255, 67, 0.69);
}
.arrow_column button:hover{
  background-color: hwb(135 2% 0% / 0.79);
  box-shadow: 0 12px 16px 0 rgba(136, 135, 135, 0.625);
}
.row:after {
content: "";
display: table;
clear: both;
}

.logo_center{
/* border: 1px solid black; */
display: inline-block;
width: 250px;
}

.register{
  /* border: 1px solid black; */
  position: relative;
  transition: transform 300ms, box-shadow 300ms;
}
.register > form{
  margin: 15% 0 5% 0;
}
.register > form > input {
  font-family: "Asap", sans-serif;
  font-style: italic;
  display: inline-flex;
  border-radius: 50px;
  font-size: 14px;
  background: white;
  width: 50%;
  border: 1px solid #ff7b00ab;
  padding:2% 0 2% 2%;
  margin:0 0 5px 0;
}
.register > form > label {
  font-family: "Asap", sans-serif;
  font-style: italic;
  display: inline-flex;
  border-radius: 50px;
  font-size: 14px;
  width: 50%;
  padding:0;
  margin:0 0 2px 0;
}
.register > form > button{
background-color: rgba(4, 255, 67, 0.69);
border: none;
font-style:normal;
font-size: 16px;
border-radius: 25px;
width:auto;
margin:3% 0 2% 0;
padding: 0 20px 0 20px;
height: 40px;
}
.register > form > button:hover {
  background-color: hwb(135 2% 0% / 0.79);
  box-shadow: 0 12px 16px 0 rgba(136, 135, 135, 0.625);
}
.register::before,
.register::after {
  content: "";
  position: absolute;
  width: 800px;
  height: 800px;
  border-top-left-radius: 35%;
  border-top-right-radius: 40%;
  border-bottom-left-radius: 45%;
  border-bottom-right-radius: 35%;
  z-index: -1;
}
.register::before {
  left: 20%;
  bottom: -80%;
  background-color:  #eeb9574b;
  animation: wawes 6s infinite;
}
.register::after {
  left: 35%;
  bottom: -90%;
  background-color:#fc464347;
  animation: wawes 7s infinite linear;
}
@keyframes wawes {
  from {
    transform: rotate(0);
  }
  to {
    transform: rotate(360deg);
  }
}

@media screen and (max-width: 750px) {
.column {
  width: 100%;
  padding: 5% 0 5% 0;
  margin:0;
}
.row{
  width: 90%;
  margin:3em auto 0 auto;
}
.logo_center{
/* border: 1px solid black; */
margin:0;
}
.register > form{
  margin: 0;
}
.register::before {
  left: 10%;
  bottom: -135%;
}
.register::after {
  left: 25%;
  bottom: -155%;
}
.register > form > input{
  width: 70%;
  font-size: 12px;
  padding:2% 0 2% 2%;
  margin:0 0 10px 0;
}
.register > form > label{
  width:70%;
  font-size:12px;
}
}
</style>