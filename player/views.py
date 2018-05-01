from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import InvitationForm
from .models import Invitation

@login_required()
def home(request):
    # games_first_player = Game.objects.filter(
    #     first_player=request.user,
    #     status='F'
    # )
    # games_second_player = Game.objects.filter(
    #     second_player=request.user,
    #     status='S'
    # )
    # all_my_games = list(games_first_player) + \
    #                 list(games_second_player)
    #
    # return render(request, "player/home.html",
    #               # count number of games in database
    #               # {'ngames': Game.objects.count() }
    #               {'games': all_my_games}
    #               )
    # above code optimized below and also added the activated user data.

    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    finished_games = my_games.difference(active_games)
    invitations = request.user.invitations_recevied.all()
    return render(request, "player/home.html",
                  {'games': active_games,
                   'finished_games': finished_games,
                   'invitation': invitations
                   }
                  )

@login_required
def new_invitation(request):
    # form = InvitationForm()
    if request.method == "POST":
        # TODO handle for submit or not handle get error CSRF token(403).
        # Here handle error for security purpose and or error CSRF token.
        # pass
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})

#
@login_required()
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)

    if request.method == 'POST':
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user
            )
        invitation.delete()
        return redirect(game)
    else:
        return render(request, "player/accept_invitation_form.html",
                      {'invitation': invitation}
                      )

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "player/signup_form.html"
    success_url = reverse_lazy('player_home')
