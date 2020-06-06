<template>
  <el-container>
    <el-header style="border: 1px solid #eee">
      <el-row>
        <el-col :span="2" :offset="22">
          <el-button type="primary" @click="test()">测试</el-button>
          <el-button type="primary" @click="addUser()">添加账号</el-button>
            <el-dialog title="添加账号" :visible.sync="dialogFormVisible" style="width:60%;left:20%" :center="true" @close='closeDialog()'>
            <el-form :model="form">
             <el-form-item label="账号" :label-width="formLabelWidth">
               <el-input v-model="form.account" autocomplete="off"></el-input>
             </el-form-item>
             <el-form-item label="密码" :label-width="formLabelWidth">
               <el-input v-model="form.password" autocomplete="off"></el-input>
             </el-form-item>
             <el-form-item label="名字" :label-width="formLabelWidth">
               <el-input v-model="form.name" autocomplete="off"></el-input>
             </el-form-item>
             <!-- <el-form-item label="属性" :label-width="formLabelWidth">
               <el-input v-model="form.name" autocomplete="off"></el-input>
             </el-form-item> -->
             <!-- <el-form-item label="属性" :label-width="formLabelWidth">
            <el-select v-model="form.type" placeholder="请选择人员属性">
              <el-option label="内部" :value="1"></el-option>
              <el-option label="外部" :value="2"></el-option>
            </el-select>
          </el-form-item> -->
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="commitUser">确 定</el-button>
        </div>
      </el-dialog>
        </el-col>
      </el-row>
    </el-header>
    <el-main style="border: 1px solid #eee">
      <el-table :data="getData" style="width: 100%">
        <el-table-column prop="id" label="用户ID" width="100"></el-table-column>
        <el-table-column prop="account" label="账号" width="150"></el-table-column>
        <el-table-column prop="name" label="名字" width="150"></el-table-column>
        <!-- <el-table-column label="属性" :formatter="statusFormat" width="150"></el-table-column>
        <el-table-column prop="groups" label="分组" width="350"></el-table-column> -->
        <el-table-column label="操作" align="center" min-width="100">
         <template slot-scope="scope">
          <el-button type="primary" @click="saveUser(scope.row.id)">修改</el-button>
          <el-button type="danger" @click="delUser(scope.row.id)">删除</el-button>
         </template>
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      getData: [],
      dialogFormVisible: false,
      form: {
        // id: 0,
        // useraccount: '',
        // password: '',
        // name: '',
        // type: '',
        // groups: 0
      },
      formLabelWidth: '120px'
    }
  },
  created () {
    var userUrl = '/users/'
    const axios = require('axios')
    axios.get(userUrl).then(res => {
      this.getData = res.data.results
    })
  },
  methods: {
    addUser () {
      this.dialogFormVisible = true
      console.log(this.form)
    },
    saveUser (id) {
      var key = 0
      for (var i = 0; i < this.getData.length; i++) {
        if (this.getData[i].id === id) {
          key = i
          break
        }
      }
      this.form = this.getData[key]
      this.dialogFormVisible = true
    },
    test () {
      var url= 'http://192.168.2.25:8080/app/alipay/addOrder?orderId=1&userId=1'
      const axios = require('axios')
      axios.post(userUrl)
    },
    delUser (id) {
      var userUrl = '/user/'
      const axios = require('axios')
      this.$confirm('此操作将删除该账号, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        axios.get(userUrl).then(res => {
          var data = res.data.data
          console.log(data)
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
        }
        )
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    commitUser () {
      var userUrl = '/user/'
      const axios = require('axios')
      var postData = {
        data: JSON.stringify(this.form),
        msg: '',
        uid: 1
      }
      axios.post(userUrl, postData).then(res => {
        var data = res.data.data
        console.log(data)
        this.$message({
          message: '提交成功',
          type: 'success'
        })
      })
      this.dialogFormVisible = false
    },
    closeDialog () {
      this.form = {}
    },
    statusFormat (row, column) {
      let type = row.type
      let typeW = '未定义'
      switch (type) {
        case 1:
          typeW = '内部'
          break
        case 2:
          typeW = '外部'
          break
      }
      return typeW
    }
  }
}
</script>
