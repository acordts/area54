import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { UpcomingComponent }      from './upcoming.component';
import { OnDemandComponent }      from './ondemand.component';
import { WebcastDetailComponent }  from './webcast-detail.component';

const routes: Routes = [
  { path: '', redirectTo: '/upcoming', pathMatch: 'full' },
  { path: 'webcast/:id', component: WebcastDetailComponent },
  { path: 'upcoming',   component: UpcomingComponent },
  { path: 'ondemand',   component: OnDemandComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
