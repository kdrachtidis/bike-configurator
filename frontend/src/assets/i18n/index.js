import { createI18n } from 'vue-i18n'

import enLocale from './en.json'
import deLocale from './de.json'
import grLocale from './gr.json'
import frLocale from './fr.json'

const defaultLocale = 'de'

export const i18n = createI18n({
  locale: defaultLocale,
  fallbackLocale: 'en',
  messages:{
      de: deLocale,
      en: enLocale,
      fr: frLocale,
      gr: grLocale
  }
})
