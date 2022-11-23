<template>
  <div class="row">
    <div class="column">
      <router-link to="/">
        <img class="logo_center" src="@/assets/logo.svg">
      </router-link>
    </div>
    <div class="column register">
      <form>
      <input type="text" id="user_name" name="user_name" placeholder="User name"><br>
      <input type="password" id="password" name="password" placeholder="Password"><br>
      <button id="submit" name="submit" value="Login">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {

}
</script>


<style scoped>
* {
box-sizing: border-box;
}
.row{
overflow: hidden;
width:70%;
margin:8em auto 0 auto;
border-radius: 50px;
box-shadow: 10px 12px 16px 0 rgba(136, 135, 135, 0.625);
}
.column {
/* border:1px solid black; */
float: left;
width: 50%;
padding: 5% 0 5% 0;
margin: 5% 0 5% 0;
/* height: 300px; Should be removed. Only for demonstration */
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
  border-radius: 5px;
  font-size: 12px;
  background: white;
  width: 50%;
  border: 3px solid #ff7b00ab;
  padding:2% 0 2% 2%;
  margin:0 0 5px 0;
}
.register > form > label {
  font-family: "Asap", sans-serif;
  font-style: italic;
  display: inline-flex;
  border-radius: 5px;
  font-size: 12px;
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

@media screen and (max-width: 900px) {
.column {
  width: 100%;
  padding: 5% 0 5% 0;
  margin: 5% 0 5% 0;
}
.row{
  width: 90%;
  margin:3.5em auto 0 auto;
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
  padding:2% 0 2% 2%;
  margin:0 0 5px 0;
}
.register > form > label{
  width:70%;
}
}
</style>