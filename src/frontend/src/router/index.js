import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/LoginView.vue"),
  },
  {
    path: "/index",
    name: "index",
    redirect: "/home",
    component: () => import("@/views/IndexView.vue"),
    children: [
      {
        path: "/home",
        name: "home",
        meta: { title: "首页", icon: "menu" },
        component: () => import("@/views/home/index.vue"),
      },
      {
        path: "/monitor/generator",
        name: "generator",
        meta: { title: "发电机监测与预警", icon: "menu" },
        component: () => import("@/views/generator/index.vue"),
      },
      {
        path: "/monitor/gearbox",
        name: "gearbox",
        meta: { title: "齿轮箱监测与预警", icon: "menu" },
        component: () => import("@/views/gearbox/index.vue"),
      },
      {
        path: "/monitor/main-bearing",
        name: "main-bearing",
        meta: { title: "主轴承监测与预警", icon: "menu" },
        component: () => import("@/views/main-bearing/index.vue"),
      },
      {
        path: "/monitor/transducer",
        name: "transducer",
        meta: { title: "变频器监测与预警", icon: "menu" },
        component: () => import("@/views/transducer/index.vue"),
      },
      {
        path: "/monitor/yaw",
        name: "yaw",
        meta: { title: "偏航系统监测与预警", icon: "menu" },
        component: () => import("@/views/yaw/index.vue"),
      },
      {
        path: "/monitor/default",
        name: "default",
        meta: { title: "默认变量监测与预警", icon: "menu" },
        component: () => import("@/views/default/index.vue"),
      },
      // {
      //   path: "/monitor/sf6",
      //   name: "sf6",
      //   meta: { title: "SF6气体监测", icon: "menu" },
      //   component: () => import("@/views/sf6/index.vue"),
      // },
      // {
      //   path: "/monitor/sound",
      //   name: "sound",
      //   meta: { title: "声音监测", icon: "menu" },
      //   component: () => import("@/views/sound/index.vue"),
      // },
      {
        path: "/monitor/overall",
        name: "overall",
        meta: { title: "综合监测与预警", icon: "menu" },
        component: () => import("@/views/overall/index.vue"),
      },
      {
        path: "/model_management",
        name: "model_management",
        meta: { title: "机器学习模型", icon: "menu" },
        component: () => import("@/views/model-management/MeasuresModel.vue"),
      },
      {
        path: "/train_logs",
        name: "train_logs",
        meta: { title: "训练日志", icon: "menu" },
        component: () => import("@/views/train_logs/index.vue"),
      },
      // {
      //   path: "/model-management",
      //   name: "model-management",
      //   meta: { title: "模型管理", icon: "menu" },
      //   children: [
      //     {
      //       path: "/model-management/measures-model",
      //       name: "measures-model",
      //       meta: { title: "单测点模型", icon: "menu" },
      //       component: () =>
      //         import("@/views/model-management/MeasuresModel.vue"),
      //     },
      //     {
      //       path: "/model-management/fusion-model",
      //       name: "fusion-model",
      //       meta: { title: "融合模型", icon: "menu" },
      //       component: () => import("@/views/model-management/FusionModel.vue"),
      //     },
      //   ],
      // },
      // {
      //   path: "/monitor/video",
      //   name: "video",
      //   meta: { title: "视频监测", icon: "menu" },
      //   component: () => import("@/views/video/index.vue"),
      // },
      // {
      //   path: "/report",
      //   name: "report",
      //   meta: { title: "预警报告", icon: "menu" },
      //   component: () => import("@/views/report/index.vue"),
      // },
      {
        path: "/user",
        name: "user",
        meta: { title: "用户管理", icon: "menu" },
        component: () => import("@/views/user/index.vue"),
      },
      // {
      //   path: "/about",
      //   name: "about",
      //   meta: { title: "关于", icon: "menu" },
      //   component: () => import("@/views/about/index.vue"),
      // },
    ],
  },
  {
    path: "/:pathMatch(.*)*", // 404
    name: "NotFound",
    component: () => import("@/views/NotFoundView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
