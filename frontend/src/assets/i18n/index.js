import { createI18n } from 'vue-i18n'

import enLocale from './en.json'
import deLocale from './de.json'
import grLocale from './gr.json'

const defaultLocale = 'de'

export const i18n = createI18n({
  locale: defaultLocale,
  fallbackLocale: 'en',
  messages:{
      en: enLocale,
      de: deLocale,
      gr: grLocale
  }
})