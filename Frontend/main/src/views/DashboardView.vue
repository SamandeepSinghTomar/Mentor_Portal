<template>
  <div class="row">
    <div class="nav">
      <router-link to="/">
        <img class="logo_center" src="@/assets/logo.svg">
      </router-link>
      <div class="nav_row">
        <button><i class="fa fa-home"></i>&nbsp;Home</button>
        <button><i class="fa fa-user"></i>&nbsp;Profile</button>
        <button><i class='fas fa-chalkboard-teacher'></i>&nbsp;Mentors</button>
        <button><i class="fa fa-comments-o"></i>&nbsp;Discourse</button>
        <button><i class="fa fa-users"></i>&nbsp;Groups</button>
        <button><i class="fa fa-video"></i>&nbsp;Meets</button>
      </div>
    </div>
    <div class="body">
      <div class="hey_box">
        <h2>Hey, {{ this.first_name }}</h2>
        <div class="search">
          <input type="text" placeholder="Search.." style="">
          <button type="reset"><i class="fa fa-filter"></i></button>
          <button type="submit"><i class="fa fa-search"></i></button>
        </div>
      </div>
      <div class="chat" style="height:75vh;">
        <p>Space for chats and posts or feeds......</p>
      </div>
    </div>
    <div class="updates">
      <div class="profile">
        <img src="@/assets/profile.jpg">
        <h4>{{this.first_name +" " + this.middle_name +" "+ this.last_name}}<br><span>{{this.role}}</span></h4>
      </div>
      <div class="calendar">
        <p>Calendar</p>
        <Calendar />
      </div>
      <div class="mentor_list">
        <p>Mentors</p>
        <ul style="text-align:left">
          <li>John Due</li>
          <li>Pauline Barmby</li>
          <li>Mathew Hic</li>
          <li>Apurva Narayan</li>
        </ul>
      </div>
  </div>
  </div>
</template>

<script>
import { Calendar } from 'v-calendar';

export default {
  data(){
    return{
      first_name:localStorage.first_name,
      middle_name:localStorage.middle_name,
      last_name:localStorage.last_name,
      role:localStorage.role,
    }
  },
  components: {
    Calendar,
  },
  beforeMount() {
    // this.$router.go(1)
    this.$router.push('/dashboard')
  },
  date: new Date(),
}
</script>

<style scoped>
.nav,.body,.updates {
  /* border: 1px solid black; */
  margin: 2% 1% 0 0;
  float: left;
  border-radius: 25px;
  box-shadow: 5px 6px 12px 4px rgba(191, 188, 188, 0.578);
}
.body{
  box-shadow: 0 0 0 0;
}
.chat,.hey_box{
  border-radius: 25px;
  box-shadow: 5px 6px 12px 4px rgba(191, 188, 188, 0.578);
}
.nav{
  margin-left: 1%;
  width:20%;
}
.nav_row{
  margin:12% 0 15% 0;
}
.nav_row button{
  width: 100%;
  font-size: 18px;
  display: inline-flex;
  border-radius: 18px;
  padding: 5% 0 5% 32%;
  /* height: 6vh; */
  /* justify-content: end; */
  border: none;
  background: none;
}
.nav_row>button>i{
  color:#7b241c;
}
.nav_row>button:hover{
  background: rgba(204, 204, 204, 0.542);
}
.body{
  width:50%
}
.hey_box{
  /* border: 1px solid black; */
  display: flex;
}
.search{
  /* border: 1px solid black; */
  width: 50%;
  display: inline-flex;
  justify-content: flex-end;
  height: max-content;
  padding:2.25% 2.5% 0 0;
}
.search input[type=text] {
  border: none;
}

.search button {
  /* border: 1px solid black; */
  background: #ddd;
  font-size: 20px;
  border: none;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  height: 35px;
  cursor: pointer;
}

.search button:hover {
  background: #ccc;
}
.search button[type="reset"]{
  border-right: 1px solid rgba(171, 171, 171, 0.415);
  border-top-right-radius: 0px;
  border-bottom-right-radius: 0px;
}
.hey_box>h2{
  /* border: 1px solid black; */
  width: 50%;
  padding: 0 3%;
  display:inline-block;text-align: left;
}
.logo_center{
  /* border: 1px solid black; */
  margin: 13% 0 0 0;width: 100px;
}
.updates{
  width: 25%;
  overflow: hidden;
}
.update:after {
  content: "";  display: table;clear: both;
}
.profile{
  /* border: 1px solid black; */
  margin:4% 0 0 4%;
  width: 92%;
  float: left;
}
.profile>img{
  width:50px;border-radius:25px;float: left;display:block;
}
.profile>h4{
  /* border:1px solid black; */
  margin:5px 0 0 0;position: relative;
}
.profile>h4>span{
  /* border:1px solid black; */
  font-size:80%;
}
.calendar{
  /* border:1px solid black; */
  display: inline-block;
  width: 100%;
}
.mentor_list{
  /* border: 1px solid black; */
}
</style>