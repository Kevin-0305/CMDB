<template>
  <div id="app" >
    <div v-show="!$route.meta.keepAlive">
    <el-row style="height:100px;margin-top:100px">
      <el-col :span="3" :offset="4">
        <div class="logo-img">
          <img src="./assets/logo.png" style="width:40px;height:40px" />
        </div>
      </el-col>
      <el-col :span="3" :offset="6">
        <li class="el-icon-user">username</li>
      </el-col>
      <el-col :span="3">
        <el-button>退出</el-button>
      </el-col>
    </el-row>
    </div>
    <el-row>
      <el-col :span="3" :offset="4">
        <el-container
          style="height: 800px;width: 1400px;text-align: center; border: 1px solid #eee"
        >
          <el-aside width="200px" style="background-color: #545c64" v-show="!$route.meta.keepAlive">
            <el-col :span="3" :offset="4">
              <el-menu
                default-active="activeIndex"
                class="el-menu-vertical-demo"
                @select="handleSelect"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b"
              >
                <el-menu-item index="/">
                    <i class="el-icon-location"></i>
                    <span>首页</span>
                </el-menu-item>
                <el-menu-item index="/users">
                  <i class="el-icon-menu"></i>
                  <span slot="title">账号管理</span>
                </el-menu-item>
                <el-menu-item index="/server">
                  <i class="el-icon-document"></i>
                  <span slot="title">服务器管理</span>
                </el-menu-item>
                <el-menu-item index="4">
                  <i class="el-icon-document"></i>
                  <span slot="title">分组管理</span>
                </el-menu-item>
              </el-menu>
            </el-col>
          </el-aside>
          <el-main>
            <router-view ></router-view>
          </el-main>
        </el-container>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      activeIndex: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key)
      this.$router.push(key)
    }
  }
}
</script>

<style>
.logo-img {
  height: 100px;
}
</style>
