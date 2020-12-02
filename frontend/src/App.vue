<template>
  <div id="app">
  
    <NavbarComponent/>

    <router-view />
  </div>
</template>

<script>
//API Servie
import {apiService} from './common/api.service'

import NavbarComponent from "./components/Navbar.vue"
export default {
  name:"App",
  components:{
    NavbarComponent
  },
  methods:{
    async setUserInfo(){
      const data = await apiService('/api/user/');
      const requestUser = data['username']
      window.localStorage.setItem('username',requestUser);
      console.log(data)
      console.log(requestUser)
    }
  },
  created(){
    this.setUserInfo()
  }
}
</script>


<style>
   *,body{
            font-family: 'Texturina', serif;
        }
</style>
