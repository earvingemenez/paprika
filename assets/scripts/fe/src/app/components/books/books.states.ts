import { ContentOnly, NavContent } from '../../commons/utils/layout.utils';
import { LoginRequired } from '../../commons/utils/security.utils';

import { SettingComponent } from './setting/setting.component';


export const BOOKS_STATES : Object[] = [
  {
    name    : 'book-setting',
    url     : '/books/:code/setting/',
    views   : NavContent(SettingComponent),
    onEnter : LoginRequired
  },
]