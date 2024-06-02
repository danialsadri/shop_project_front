from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from .forms import ContactUsForm, NewsLetterForm


class IndexView(View):
    def get(self, request):
        return render(request, 'website/index.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'website/about.html')


class ContactUsView(View):
    form_class = ContactUsForm
    template_name = 'website/contact_us.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تیکت شما با موفقیت ثبت شد و در اسرع وقت با شما تماس حاصل خواهد شد')
            return redirect('website:contact_us')
        else:
            messages.error(request, 'مشکلی در ارسال فرم شما پیش آمد لطفا ورودی ها رو بررسی کنین و مجدد ارسال نمایید')
        return render(request, self.template_name, {'form': form})


class NewsletterView(View):
    def post(self, request):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'از ثبت نام شما ممنونم، اخبار جدید رو براتون ارسال می کنم 😊👍')
            return redirect('website:index')
        messages.error(self.request, 'مشکلی در ارسال فرم شما وجود داشت که می دونم برا چی بود!! چون ربات هستید!')
        return redirect('website:index')
