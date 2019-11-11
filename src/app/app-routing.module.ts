import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TradingviewComponent } from './tradingview/tradingview.component'
import { PageNotFoundComponent } from './error/page-not-found/page-not-found.component'
import { AppComponent } from './app.component';

const routes: Routes = [
  { path: '', component: AppComponent },
  { path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
