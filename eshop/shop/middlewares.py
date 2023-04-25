from django.shortcuts import redirect


def auth_middleware(get_response):
    

    def middleware(request):
        print("middleware")
        
        if not request.session.get('id'):
            
            return redirect('login')

        response = get_response(request)
        return response

    return middleware