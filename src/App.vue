<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/connector">Connector</router-link>
    </div>
    <div id="container" ref="container">
      <div id="settings">
        <h1>Connectors</h1>
        <span v-on:click="req('CSV')">CSV</span>
        <span v-on:click="req('Excel')">Excel</span>
        <span v-on:click="req('Postgres')">Postgres</span>
      </div>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Connector from '@/components/connector.vue'
import Vue from 'vue'
import axios from 'axios'

export default {
  methods: {
    req: function (path) {
      axios
        .get('http://localhost:5000/connector/' + path)
        .then(response => console.log(response))
      // TODO Do this with py backend
      Connector.props.connName = path
      var ComponentClass = Vue.extend(Connector)
      var instance = new ComponentClass({})
      instance.$mount() // pass nothing
      this.$refs.container.appendChild(instance.$el)
    }
  }
}
</script>

<style>
#app {
  height: 100%;
  display: flex;
  flex-direction: column;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#nav {
  background-color: #2c3e50;
  padding: 30px;
  color: white;
  text-align: center;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: orange;
}

#container {
  height: 100%;
  display: flex;
}

#settings {
  flex-basis: 10em;
  display: flex;
  flex-direction: column;
  padding: 1vh 2vw;
  background-color: orange;
}

#settings span {
  margin: 0.2vh 0;
}
</style>
