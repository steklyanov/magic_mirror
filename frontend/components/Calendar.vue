<template>
  <v-container>
    <v-sheet
      tile
      height="54"
      color="grey lighten-3"
      class="d-flex"
    >
      <v-btn
        icon
        class="ma-2"
        @click="switchToThePrevMonth"
      >
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <v-select
        v-model="type"
        :items="types"
        dense
        outlined
        hide-details
        class="ma-2"
        label="type"
      />
      <v-select
        v-model="mode"
        :items="modes"
        dense
        outlined
        hide-details
        label="event-overlap-mode"
        class="ma-2"
      />
      <v-select
        v-model="weekday"
        :items="weekdays"
        dense
        outlined
        hide-details
        label="weekdays"
        class="ma-2"
      />
      <v-spacer />
      <v-btn
        icon
        class="ma-2"
        @click="switchToTheNextMonth"
      >
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-sheet>
    <v-sheet height="600">
      <v-calendar
        ref="calendar"
        v-model="value"
        :weekdays="weekday"
        :type="type"
        :events="events"
        :event-overlap-mode="mode"
        :event-overlap-threshold="30"
        @change="getEvents"
      />
    </v-sheet>
  </v-container>
</template>

<script>

export default {
  name: 'Calendar',
  data () {
    return {
      year_start: 0,
      month_start: 0,
      day_start: 0,
      year_end: 0,
      month_end: 0,
      day_end: 0,
      show: false,
      type: 'month',
      types: ['month', 'week', 'day', '4day'],
      mode: 'stack',
      modes: ['stack', 'column'],
      weekday: [0, 1, 2, 3, 4, 5, 6],
      date: null,
      weekdays: [
        { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
        { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
        { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
        { text: 'Mon, Wed, Fri', value: [1, 3, 5] }
      ],
      value: '',
      events: [],
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1']
    }
  },
  created () {
    this.date = new Date()
    this.getEvents()
  },
  methods: {
    setPeriod () {
      this.month_start = String(this.date.getMonth() + 1).padStart(2, '0')
      this.year_start = this.date.getFullYear()
      this.day_start = 1
      this.day_end = new Date(this.year_start, this.month_start, 0).getDate()
      this.month_end = this.month_start
      this.year_end = this.year_start
    },
    switchToTheNextMonth () {
      this.$refs.calendar.next()
      if (this.date.getMonth() === 11) {
        this.date = new Date(this.date.getFullYear() + 1, 0, 1)
      } else {
        this.date = new Date(this.date.getFullYear(), this.date.getMonth() + 1, 1)
      }
    },
    switchToThePrevMonth () {
      this.$refs.calendar.prev()
      if (this.date.getMonth() === 1) {
        this.date = new Date(this.date.getFullYear() - 1, 12, 1)
      } else {
        this.date = new Date(this.date.getFullYear(), this.date.getMonth() - 1, 1)
      }
    },
    async getEvents () {
      await this.setPeriod()

      const payload = '/event/list?ms=' + this.month_start +
        '&ys=' + this.year_start +
        '&ds=' + this.day_start +
        '&me=' + this.month_end +
        '&ye=' + this.year_end +
        '&de=' + this.day_end
      this.$axios.$get(payload).then((response) => {
        // eslint-disable-next-line no-console
        console.log(response)
        this.events = []
        response.forEach((res) => {
          this.events.push({
            name: res.name,
            start: res.start_date + ' ' + res.start_time,
            end: res.end_date + ' ' + res.end_time,
            color: this.colors[1]
          })
        })
      }).catch((e) => {
        // eslint-disable-next-line no-console
        console.log(e)
      })
    }
  }
}
</script>

<style scoped>

</style>
