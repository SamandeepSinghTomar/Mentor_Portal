<template>
    <div class="row">
      <div class="arrow_column">
        <button href="#" style="text-decoration:none;color:white;" @click="$router.go(-1)">&lt;</button>
      </div>
      <div class="column">
        <router-link to="/">
          <img class="logo_center" src="@/assets/logo.svg">
        </router-link>
        <p style="font-style:italic;">Already a User? <router-link to="/login" style="color:rgba(0, 255, 136);text-decoration: none;">Login</router-link></p>
      </div>
      <div class="column register">
        <form>
        <input type="text" id="first_name" name="first_name" placeholder="First Name"><br>
        <input type="text" id="middle_name" name="middle_name" placeholder="Middle name"><br>
        <input type="text" id="last_name" name="last_name" placeholder="Last name"><br>
        <input type="text" id="user_name" name="user_name" placeholder="User name"><br>
        <input type="text" placeholder="Date of Birth" onfocus="(this.type='date')" id="dob" name="dob"><br>
        <input type="email" id="email" name="email" placeholder="Email Address"><br>
        <input type="password" id="password" name="password" placeholder="Password"><br>
        <input type="password" id="re_password" name="re_password" placeholder="Re-Enter Password"><br>
        <label for="role" style="margin:0 2% 0 2%;">Role</label><br>
        <select name="role" size="1">
          <option id="student" name="role" key="Student">Student</option>
          <option id="mentor" name="role" key="Mentor">Mentor</option>
          <option id="alumni" name="role" key="alumni">Alumni</option>
        </select>
        <br>
        <button id="submit" name="submit" value="Register">Register</button>
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
  margin:5em auto 0 auto;
  border-radius: 50px;
  box-shadow: 10px 12px 16px 0 rgba(136, 135, 135, 0.625);
}
.column {
  /* border:1px solid black; */
  float: left;
  width: 50%;
  padding: 3% 0 2% 0;
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
  background-color: rgba(0, 118, 253, 0.536);
}
.arrow_column button:hover{
  box-shadow: 0 12px 16px 0 rgba(136, 135, 135, 0.625);
}
.row:after {
  content: "";
  display: table;
  clear: both;
}

.logo_center{
  /* border: 1px solid black; */
  margin:10% 0 0 0;
  display: inline-block;
  width: 250px;
}

.register{
  /* border: 1px solid black; */
    position: relative;
    transition: transform 300ms, box-shadow 300ms;
}
.register > form > input {
    font-family: "Asap", sans-serif;
    font-style: italic;
    display: inline-flex;
    border-radius: 50px;
    font-size: 14px;
    background: white;
    width: 50%;
    border: 1px solid rgba(0, 255, 136, 0.411);
    padding:2% 0 1% 2%;
    margin:0 0 5px 0;
  }
  .register > form > select{
    font-family: "Asap", sans-serif;
    font-style: italic;
    display: inline-flex;
    border-radius: 50px;
    font-size: 14px;
    background: white;
    width: 50%;
    border: 1px solid rgba(0, 255, 136, 0.411);
    margin:0 0 5px 0;
    padding: 1% 0 1% 2%;
  }
  .register > form > label {
    font-family: "Asap", sans-serif;
    font-style: italic;
    display: inline-flex;
    border-radius: 50px;
    font-size: 14px;
    width: 50%;
    padding:0 0 0 5px;
    margin:0 0 2px 0;
  }
  .register > form > button {
  background-color: #ff7b00ab;
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
    background-color: #ff7b00c6;
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
    padding: 1% 0 2% 0;
  }
  .column p{
    font-size: smaller;
  }
  .row{
    width: 90%;
    margin:2em auto 0 auto;
  }
  .logo_center{
  /* border: 1px solid black; */
  margin:0;
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
    font-size: 12px;
    width: 70%;
    padding:1% 0 1% 2%;
    margin:0 0 5px 0;
  }
  .register > form > label{
    width:70%;
    font-size: 12px;
  }
  .register > form > select{
    width: 70%;
    font-size: 12px;
    padding: 1% 0 1% 2%;
  }
}
</style>