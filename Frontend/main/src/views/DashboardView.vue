<template>
  <div class="row">
    <div class="nav">
      <router-link to="/">
        <img class="logo_center" src="@/assets/logo.svg">
    </router-link>
    </div>
    <div class="body">
      <h2 style="display:flex;justify-content:left;">Hey, First Name</h2>
    </div>
    <div class="updates">
      <div class="profile">
        <img src="@/assets/profile.jpg">
        <h4>Full Name<br><span>Role</span></h4>
      </div>
      <div class="calendar">
        <p>Calendar</p>
      </div>
  </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.nav,.body,.updates {
  border: 1px solid black;float: left;
}
.nav{
  width:20%;
}
.body{
  width:60%
}
.updates{
  width: 19%;
}
.row:after {
  content: "";  display: table;clear: both;
}
.logo_center{
  border: 1px solid black;margin: 4% 0 0 0;width: 80px;
}
.profile>img{
  width:50px;border-radius:25px;float: left;
}
.profile>h4{
  border:1px solid black;float:right;margin:5px 0 0 0;
}
.profile>h4>span{
  font-size:80%;border:1px solid black;
}
</style>