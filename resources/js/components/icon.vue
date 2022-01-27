<template>
  <n-icon v-bind="props">
    <icon />
  </n-icon>
</template>

<script setup>
import { NIcon } from 'naive-ui'
import {
  ArrowSync20Regular as refresh,
  DataUsage24Regular as dashboard,//Home24Regular
  Compose20Regular as posts,
  News20Regular as pages,
  ImageMultiple24Regular as media,
  People24Regular as users,
  Person24Regular as user,
  BookContacts28Regular as clients,
  Comment20Regular as comments,
  Color20Regular as themes,
  AppFolder20Regular as plugins,
  Toolbox20Regular as tools,
  Settings20Regular as settings,
  Add20Filled as add,
  ChatHelp20Regular as help,
  Alert20Regular as notifications,
  Warning24Regular as fallback,
  CalendarLtr28Regular as calendar,
  CalendarPerson24Regular as calendar_person,
  CalendarSettings16Regular as calendar_settings,
  CalendarSync20Regular as calendar_sync,
  PeopleTeam24Regular as team, //ContactCardGroup28Regular
  TasksApp28Regular as services,
  PreviewLink20Regular as preview_link,
  SignOut20Regular as logout,
  BuildingShop24Regular as company,
  Shifts24Regular as shifts,
  ShiftsOpen20Regular as shifts_open,
  ShiftsTeam24Regular as shifts_team,
  Code20Filled as code,
  MoreVertical24Regular as more
} from '@vicons/fluent'

import { LogoGoogle as google, LogoFacebook as facebook } from '@vicons/ionicons5'

const icons = { refresh, dashboard, posts, pages, media, users, comments, themes, plugins, tools, settings, add, help, notifications, fallback, calendar, users, user, services, logout, clients, company, calendar_person, calendar_sync, calendar_settings, team, preview_link, shifts, shifts_open, shifts_team, code, more, google, facebook }

const props = defineProps({
  ...NIcon.props,
  type: {
    type: String,
    default: 'fallback'
  }
})

const icon = icons[props.type]
</script>