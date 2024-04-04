<script setup>
import { ref, reactive, onMounted, watch, onBeforeUnmount, provide } from "vue";
import { getMeasuresInfo } from "@/api/measures";
import DataTable from "@/components/DataTable.vue";
import TrainAllButton from "@/components/TrainAllButton.vue";
import { formatNumber } from "@/utils/index";

const data = ref([]);
const form = reactive({
  plant: "画笔山风电场",
  unit: "#1号机组",
});

const setData = async () => {
  await getMeasuresInfo(form.plant + "&" + form.unit + "&" + "变频器").then(
    (res) => {
      if (res.code === 200) {
        // console.log(res.data);
        data.value = res.data
          .map((item) => {
            return {
              key: item.key,
              path: item.path.split("_")[item.path.split("_").length - 1],
              // time: item.time.replace("T", " ").split(".")[0],
              time: item.service_time?.replace("T", " ").split(".")[0],
              service_time: item.service_time?.replace("T", " ").split(".")[0],
              value: formatNumber(item.value),
              unit: item.unit,
              status:
                item.status === 0
                  ? "模型未训练"
                  : item.status === 1
                    ? "正常"
                    : item.status === 2
                      ? "预警"
                      : item.status === 3
                        ? "报警"
                        : "未知",
              model_name: item.model_name,
              model_is_trained: item.model_is_trained,
              model_updated_at: item.model_updated_at
                ?.replace("T", " ")
                .split(".")[0],
              model_version: item.model_version,
              train_data_total: item.train_data_total,
            };
          })
          .sort((a, b) => {
            return a.key - b.key;
          });
      }
    },
  );
};

watch(
  () => form,
  () => {
    setData();
  },
  { deep: true },
);

let interval = null;
onMounted(() => {
  setData();
  interval = setInterval(() => {
    setData();
  }, 10000);
});

onBeforeUnmount(() => {
  clearInterval(interval);
});
</script>

<template>
  <!-- 搜索框 -->
  <div class="input_box">
    <el-form :inline="true" :model="form">
      <el-form-item label="风电场">
        <el-select
          v-model="form.plant"
          placeholder="请选择风电场"
          clearable
          style="width: 270px"
        >
          <el-option label="画笔山风电场" value="画笔山风电场" />
        </el-select>
      </el-form-item>
      <el-form-item label="机组">
        <el-select
          v-model="form.unit"
          placeholder="请选择机组"
          clearable
          style="width: 270px"
        >
          <el-option label="#1号机组" value="#1号机组" />
          <el-option label="#2号机组" value="#2号机组" />
          <el-option label="#3号机组" value="#3号机组" />
          <el-option label="#4号机组" value="#4号机组" />
          <el-option label="#5号机组" value="#5号机组" />
          <el-option label="#6号机组" value="#6号机组" />
          <el-option label="#7号机组" value="#7号机组" />
          <el-option label="#8号机组" value="#8号机组" />
          <el-option label="#9号机组" value="#9号机组" />
          <el-option label="#10号机组" value="#10号机组" />
          <el-option label="#11号机组" value="#11号机组" />
          <el-option label="#12号机组" value="#12号机组" />
          <el-option label="#13号机组" value="#13号机组" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="setData">更新数据</el-button>
        <TrainAllButton :data="data" @set-data="setData" />
      </el-form-item>
    </el-form>
  </div>
  <!-- 数据展示 -->
  <DataTable
    :title="`${form.plant}${form.unit}变频器在线监测`"
    :data="data"
    @set-data="setData"
  />
</template>

<style scoped></style>
