---
title: Crafts
---

<script setup>
  import { data } from './[id].data.js'
  import { useData } from 'vitepress'

  const { page } = useData()
</script>

# {{ $params.id[0].toUpperCase()+$params.id.slice(1).replace(/_/g, ' ') }}
<br/>

<li v-for="item in data" class="contains-task-list">
  <a :href=item.url v-if="item.tags.split(',').includes(page.params.id)" :style="{color: item.read ? 'rgb(255, 200, 155)' : 'rgb(168, 230, 255)'}"> {{item.title}} </a>
</li>