import {createSelector} from "@ngrx/store";
import {selectAppState} from "../../app-state/app-selectors/app.selectors";
import {AppState} from "../../app-state/app-reducers/app.reducers";
import {Breadcrumb} from "./breadcrumb.model";
import {RolesName} from "../../../enums/roles";
import {ActivatedRouteSnapshot} from "@angular/router";

export const selectRouterState = createSelector(
  selectAppState,
  (s : AppState) => s.router['state'].root
)

export const selectBreadcrumb = createSelector(
  selectRouterState,
  (s) : Array<Breadcrumb> => {
    const breadcrumbs: Breadcrumb[] = [];
    function buildBreadcrumb(k: ActivatedRouteSnapshot | null){
      k?.url.forEach((route,index) => {
        if(!Object.keys(RolesName).map(value => value.replace('_','')).includes(route.path.toUpperCase())){
          if(k?.params['id']){
            breadcrumbs.push({
              path: index === 0 ? k?.data['breadcrumb'] : route.path,
              url: breadcrumbs[breadcrumbs.length-1].url + route.path + '/'
            })
          }else{
            breadcrumbs.push({
              path: route.path,
              url: breadcrumbs.map(x => x.url+'/').toString().replace(',','') + k?.url.map(x => x.path+'/').toString().replace(',','')
            })
          }
        }
      })
      if(k?.firstChild?.routeConfig?.path){
        buildBreadcrumb(k.firstChild)
      }
    }
    buildBreadcrumb(s.firstChild)
    return breadcrumbs
  }
)
