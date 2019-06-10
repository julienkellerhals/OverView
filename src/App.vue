<template>
  <div id="app">
    <div id="nav">
      <router-link to="/connector">Connector</router-link>
    </div>
    <div id="container" ref="container">
      <div id="settings">
        <h1>Connectors</h1>
        <span v-on:click="req('CSV')" @click="showModal">CSV</span>
        <span v-on:click="req('Excel')" @click="showModal">Excel</span>
        <span v-on:click="req('Postgres')" @click="showModal">Postgres</span>
      </div>
      <router-view/>
    </div>
    <!-- TODO find out how to create modal relative to connector -->
    <modal v-show="isModalVisible" @close="closeModal"/>
  </div>
</template>

<script>
import modal from './components/Modal.vue'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    modal
  },
  data () {
    return {
      isModalVisible: false
    }
  },
  methods: {
    showModal () {
      this.isModalVisible = true
    },
    closeModal () {
      this.isModalVisible = false
    },
    req (path) {
      axios
        .get('http://localhost:5000/connector/' + path + '/add')
        .then(response => console.log(response))
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
