<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const menus = router.options.routes.filter(
  (route) => route.path === "/index",
)[0].children;
</script>

<template>
  <!-- 左侧菜单 -->
  <el-aside class="aside">
    <el-menu default-active="2" router>
      <div class="logo">
        <img src="@/assets/tianjin2.svg" alt="logo" />
        <img src="@/assets/csust.svg" alt="logo" />
      </div>
      <!-- <div class="logo"> -->
      <!--   <img src="@/assets/stategrid-full.svg" alt="logo" /> -->
      <!-- </div> -->

      <div v-for="item in menus" :key="item.path">
        <!-- 无子菜单 -->
        <el-menu-item :index="item.path" v-if="!item.children">
          <el-icon>
            <component :is="item.meta.icon" />
          </el-icon>
          {{ item.meta.title }}
        </el-menu-item>
        <!-- 有子菜单 -->
        <el-sub-menu :key="item.path" :index="item.path" v-else>
          <template #title>
            <el-icon>
              <component :is="item.meta.icon" />
            </el-icon>
            <span>{{ item.meta.title }}</span>
          </template>
          <el-menu-item
            v-for="child in item.children"
            :key="child.path"
            :index="child.path"
          >
            <el-icon>
              <component :is="item.meta.icon" />
            </el-icon>
            {{ child.meta.title }}
          </el-menu-item>
        </el-sub-menu>
      </div>
    </el-menu>
  </el-aside>
</template>

<style scoped>
.aside {
  width: 230px;
  position: sticky;
  top: 0;
  height: 100vh;
  /* 菜单栏的高度 */
  /* 菜单栏的宽度 */
  overflow-y: auto;
  /* 当内容溢出时显示滚动条 */
}

.logo {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 60px;
  margin: 20px 0;
}

.logo img {
  width: 35%;
}

.el-menu {
  background-color: #545c6410;
  border-color: #545c6420;
  height: 100vh;
  --el-menu-bg-color: #409eff20;
  --bg-color: #545c6410;
  --text-color: #fff;
  --active-color: #409eff;
  --el-menu-item-font-size: 16px;
}
</style>
