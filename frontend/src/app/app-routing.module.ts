import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { HTTP_INTERCEPTORS } from "@angular/common/http";

import { TokenInterceptorService } from "../service/token-interceptor.service";
import { AuthGuard } from "./auth.guard";

import { LoginComponent } from "./components/templates/login/login.component";
import { RegisterComponent } from "./components/templates/register/register.component";
import { ConsultationListComponent } from "./components/templates/consultation-list/consultation-list.component";
import { ConsultationCreateComponent } from "./components/templates/consultation-create/consultation-create.component";

const routes: Routes = [
  { path: 'home', component: ConsultationListComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'create', component: ConsultationCreateComponent, canActivate: [AuthGuard] },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptorService,
      multi: true
    }
  ],
})
export class AppRoutingModule { }
