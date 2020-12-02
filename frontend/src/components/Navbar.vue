
<template>
    <!--Navbar-->

    <nav class="navbar navbar-expand-lg navbar-dark bg-primary" style="padding:0rem !important;">
        <div class="container">
                    
  <!-- <a class="navbar-brand" href="#">Navbar</a>
 -->
  <router-link :to="{name:'Home'}" class="navbar-brand">Ask Anything </router-link>
    <!-- <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button> -->

  <div class="collapse navbar-collapse" id="navbarColor01">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item active">
       <router-link :to="{name:'Home'}" class="nav-link">Home </router-link>
      </li>
      <li class="nav-item">
        <router-link :to="{name:'About'}" class="nav-link">About </router-link>
      </li>

   <li class="nav-item">
        <router-link :to="{name:'Question_Edit'}" class="nav-link">Ask </router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/accounts/logout/">Logout</a>
      </li>
    
    
    </ul>
 
  </div>
        </div>
    </nav>

    <!--navbar-->
</template>

<script>
export default {
    name: "NavbarComponent"
}
</script>

<style>

</style>