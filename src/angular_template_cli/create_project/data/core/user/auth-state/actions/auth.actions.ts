import { createAction, props } from '@ngrx/store'
import { UserItem } from '../../user.model'

export const loginUser = createAction('[AUTH] login', props<{ email: string | null, publicAddress: string | null}>())
export const storeUser = createAction('[AUTH] store user', props<UserItem>())
export const clearUser = createAction('[AUTH] clear user')
